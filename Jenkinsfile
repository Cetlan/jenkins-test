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
        stage("Coverage Report") {
            steps {
                withPythonEnv("System-CPython-2.7") {
                    sh 'coverage xml'
                }
                publishCoverage adapters: [coberturaAdapter('**/coverage.xml')], calculateDiffForChangeRequests: true, failBuildIfCoverageDecreasedInChangeRequest: true, failNoReports: true, failUnstable: true, globalThresholds: [[failUnhealthy: true, thresholdTarget: 'Aggregated Report', unstableThreshold: 86.0]], sourceFileResolver: sourceFiles('STORE_LAST_BUILD')
            }
        }
    }
}
