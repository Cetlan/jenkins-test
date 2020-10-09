node {
  checkout scm
  withPythonEnv('System-CPython-2.7') {
    stage 'Setup virtual env'
    sh 'pip install coverage'
    
    stage 'Unittests'
    sh 'coverage run -m unittest discover'    
  }
}
