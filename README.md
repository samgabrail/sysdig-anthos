# Sysdig Demo on Anthos

This will automatically build using jenkins on push to github. We needed to disable SSL verification at the Github side because Jenkins is using a self-assigned certificate.

Demo of CI/CD workflow with sysdig scanning
Follow these instructions to install the Sysdig Secure plugin:
https://wiki.jenkins.io/display/JENKINS/Sysdig+Secure+Jenkins+Plugin


## gcloud authentication
On the jenkins machine do the following:
```
ubuntu@ip-10-0-0-35:/var/lib/jenkins/workspace/sysdig-jenkins-demo-pipline$ sudo su jenkins
jenkins@ip-10-0-0-35:~/workspace/sysdig-jenkins-demo-pipline$ gcloud auth login
Go to the following link in your browser:
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

You are now logged in as [sam.gabrail@sysdig.com].
Your current project is [None].  You can change this setting by running:
  $ gcloud config set project PROJECT_ID
jenkins@ip-10-0-0-35:~/workspace/sysdig-jenkins-demo-pipline$ gcloud config set project vibrant-tree-219615
Updated property [core/project].
```



