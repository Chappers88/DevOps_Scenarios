# Scenario 1: Greet user after every successful push to the repository within the logs
# Successful test

name: hello user

on:
  push:

jobs:
  hello-user-job:
    runs-on: windows-latest

    steps:
      - name: Check out repository code
        uses: actions/checkout@v4

      - name: Greet the user
        run: echo "Hello, User! CI/CD pipeline ran successfully 🚀"


# Scenario 2: Greet user after every successful push to the repository within the logs
# Failed test (searching for txt file which doesn't exist.)

name: hello user

on: push

jobs:
  hello-user-job:

  runs:on: windows-latest

   steps:
      - name: Check out repository code
        uses: actions/checkout@v4

      - name: Greet the user
        run: echo "$(cat hello_user.txt)"