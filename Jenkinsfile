node {
  checkout scm
  withPythonEnv('System-CPython-2.7') {
    stage 'Setup virtual env'
    sh 'pip install coverage'
    
    stage 'Unittests'
    sh 'coverage run -m unittest discover'    
    sh 'coverage xml'
  }

    post {
        always {
            step([$class: 'CoberturaPublisher', autoUpdateHealth: false, autoUpdateStability: false, coberturaReportFile: '**/coverage.xml', failUnhealthy: false, failUnstable: false, maxNumberOfBuilds: 0, onlyStable: false, sourceEncoding: 'ASCII', zoomCoverageChart: false])
        }
    }}
