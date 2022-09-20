import yaml
from os import path
from kubernetes import client, config


def apply_yaml():
    config.load_config()
    f = open(path.join(path.dirname(__file__), "pod.yaml"))
    pod_yaml = yaml.safe_load(f)
    v1 = client.CoreV1Api()
    try:
        # db update to in process
        resp = v1.create_namespaced_pod(body=pod_yaml, namespace="default")
        print("Pod created. status='%s'" % resp.metadata.name)
        return True
    except:
        # db update to failed
        return False


def write_yaml(**kwargs):
    template = """apiVersion: v1
kind: Pod
metadata:
  generateName: test-pod-
spec:
  restartPolicy: OnFailure
  containers:
  - name: "executor"
    image: doittemp.azurecr.io/executor-image
    command: ['python3', 'executor.py', '{serialized}']
    resources:
      requests:
        memory: "{mem}Mi"
        cpu: "{cpu}m"
  imagePullSecrets:
  - name: regcred
        """
    yfile = open(path.join(path.dirname(__file__), "pod.yaml"), "w+")
    yfile.write(template.format(**kwargs))

    print(template.format(**kwargs))
