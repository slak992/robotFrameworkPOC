import os
from datetime import datetime
from pabot import pabot
from robot import run
from robot import run_cli

def run_tests(runner,folder_path):
    # Create a dynamic output directory
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = f"tests/reports/{timestamp}"
    os.makedirs(output_dir, exist_ok=True)


    if runner=="pabot":
        # Define arguments for pabot

        # pabot_args = [
        #     "--outputdir", output_dir,
        #     "--processes", "4",
        #     "--testlevelsplit",
        #     "--output", "output.xml",
        #     "--log", "log.html",
        #     "--report", "report.html",
        #     "tests/"  # Path to the test suite folder
        # ]

        test_file = os.path.join("tests", "testDemo1.robot")
        # pabot_args = [
        #     "--outputdir", output_dir,
        #     "--processes", "4",
        #     '--test', 'Check whether the cart is displayed in the home page',
        #     "--output", "output.xml",
        #     "--log", "log.html",
        #     "--report", "report.html",
        #     test_file  # Path to the test suite folder
        # ]

        pabot_args = [
            "--outputdir", output_dir,
            "--processes", "4",
            "--include","smoke",
            "--output", "output.xml",
            "--log", "log.html",
            "--report", "report.html",
            "tests/"  # Path to the test suite folder
        ]

        # Run pabot with the specified arguments
        pabot.main(pabot_args)
    if runner=="robot":
        #run a specific test
        test_file = os.path.join("tests", "testDemo1.robot")
        #result = run(test_file, variable=['BROWSER:chrome'], outputdir=output_dir)
        ##########################################################################################################
        # #Including specific test case
        # robot_args = [
        #     '--outputdir',output_dir,
        #     '--test', 'Check whether the cart is displayed in the home page',
        #     test_file
        # ]
        ##########################################################################################################
        # #Include one tag
        # robot_args = [
        #     '--outputdir',output_dir,
        #     '--include', 'smoke',
        #     "tests/"
        # ]
        ##########################################################################################################
        # # Include tags AND
        # robot_args = [
        #     '--outputdir', output_dir,
        #     '--include', 'smokeANDregrssion',
        #     "tests/"
        # ]
        ##########################################################################################################
        # # Include tags OR
        # robot_args = [
        #     '--outputdir', output_dir,
        #     '--include', 'smokeORregrssion',
        #     "tests/"
        # ]
        ##########################################################################################################
        # # Include tags exclude
        # robot_args = [
        #     '--outputdir', output_dir,
        #     '--exclude', 'smoke',
        #     "tests/"
        # ]
        ##########################################################################################################
        # robot_args = [
        #     '--outputdir', output_dir,
        #     '--dryrun',
        #     "tests/"
        # ]
        ##########################################################################################################
        rerun_test_folder_path = os.path.join(output_dir,'output.xml')
        rerun_output_dir = os.path.join(output_dir,'rerun_output.xml')
        robot_args = [
            '--outputdir', output_dir,
            '--suite','testDemo3',
            "tests/"
        ]
        run_cli(robot_args,exit=False)
        return [rerun_test_folder_path,rerun_output_dir]
    if runner == 'rerun':
        robot_args = [
            '--rerunfailed', folder_path[0],
            '--output', folder_path[1],
            "tests/"
            ]
        result = run_cli(robot_args)



        if result == 0:
            print("Robot tests completed successfully.")
        else:
            print(f"Robot tests failed with return code {result}")

if __name__ == "__main__":
    import os
    print(os.getcwd())
    print(os.path.exists("tests/testDemo1.robot"))
    run_tests("pabot", [])
    # folder_path = run_tests("robot",[])
    # run_tests("rerun",folder_path)
