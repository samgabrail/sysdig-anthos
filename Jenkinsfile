node {
    stage('Checkout') {
        def GITHASH = checkout(scm).GIT_COMMIT
        env.GITID = GITHASH.take(7)
        sh "echo ${GITID}"
    }
    stage('Build Image') {
        sh '''
            # find the short git SHA
            #whoami
            #docker version
            echo ${BUILD_NUMBER}
            echo ${GITID}
            #GITID=$(echo ${GIT_COMMIT} | cut -c1-7)
            #echo ${GITID}
            # build the demo using the existing Dockerfile and tag the image with the short git SHA
            docker build -t gcr.io/vibrant-tree-219615/sysdig-anthos-dev:${GITID} .            
        '''
    }
    stage('Push Image to Dev') {
            sh '''
                docker push gcr.io/vibrant-tree-219615/sysdig-anthos-dev:${GITID}
                # add image to sysdig_secure_images file
                echo gcr.io/vibrant-tree-219615/sysdig-anthos-dev:${GITID} > sysdig_secure_images
            '''

    }
    stage('Scanning Image') {
        sysdigSecure 'sysdig_secure_images'
    }
    stage('Push Successfully Scanned Image to Prod') {
        sh '''
            # docker tag the dev image to prod image
            docker tag gcr.io/vibrant-tree-219615/sysdig-anthos-dev:${GITID} gcr.io/vibrant-tree-219615/sysdig-anthos-prod:${GITID}
            docker push gcr.io/vibrant-tree-219615/sysdig-anthos-prod:${GITID}           
        '''
    }
    stage('Deploy App') {
        sh '''
            # deploy the app
            gcloud container clusters get-credentials cluster-1 --zone us-central1-a --project vibrant-tree-219615
            kubectl set image deployment/sysdig-anthos sysdig-anthos=gcr.io/vibrant-tree-219615/sysdig-anthos-prod:${GITID} -n sysdig-anthos
        '''
    }
}


