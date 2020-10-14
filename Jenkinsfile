pipeline {
    agent any
    stages {
        stage("Checkout") {
            steps {
                checkout scm
            }
        }
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
        stage("Coverage") {
            steps {
                withPythonEnv("System-CPython-2.7") {
                    sh 'coverage xml'
                }
                publishCoverage adapters: [istanbulCoberturaAdapter(path: '**/coverage.xml', thresholds: [[thresholdTarget: 'Aggregated Report', unstableThreshold: 95.0]])], calculateDiffForChangeRequests: true, failBuildIfCoverageDecreasedInChangeRequest: true, failUnhealthy: true, failUnstable: true, globalThresholds: [[thresholdTarget: 'Aggregated Report', unstableThreshold: 90.0]], sourceFileResolver: sourceFiles('STORE_LAST_BUILD')
            }
        }
    }
}
