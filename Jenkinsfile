pipeline {
    agent any
    stages {
        stage("Setup Virtual Environment") {
            steps {
                withPythonEnv("System-CPython-2.7") {
                    sh 'pip install coverage'
                }
            }
        }
        stage("Unit Tests") {
            steps {
                withPythonEnv("System-CPython-2.7") {
                    sh 'coverage run -m unittest discover'
                }
            }
        }
    }
    post {
        always {
            withPythonEnv("System-CPython-2.7") {
                sh 'coverage xml'
            }
            step([$class: 'CoberturaPublisher', autoUpdateHealth: false, autoUpdateStability: false, coberturaReportFile: '**/coverage.xml', failUnhealthy: false, failUnstable: false, maxNumberOfBuilds: 0, onlyStable: 
false, sourceEncoding: 'ASCII', zoomCoverageChart: false])
        }
    }
}
