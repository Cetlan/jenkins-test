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
            publishCoverage adapters: [istanbulCoberturaAdapter(path: '**/coverage.xml', thresholds: [[thresholdTarget: 'Aggregated Report', unstableThreshold: 85.0]])], calculateDiffForChangeRequests: true, failBuildIfCoverageDecreasedInChangeRequest: true, sourceFileResolver: sourceFiles('NEVER_STORE')
        }
    }
}
