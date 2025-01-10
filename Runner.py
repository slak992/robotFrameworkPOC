import argparse
import json
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


def pabot_arg_config(args):
    pabot_args = [
        "--outputdir", args["--outputdir"],
        "--processes", args["--processes"],
        "--output", "output.xml",
        "--log", "log.html",
        "--report", "report.html",
        args["test_folder_path"]
    ]
    for arg_key,arg_value in args.items():
        if arg_value == "NO_Value":
            pabot_args.append(arg_key)

        elif arg_value not in pabot_args:

            pabot_args.extend(["--"+arg_key,arg_value])
        else:
            print("Invalid argument")
    return pabot_args

def main():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = f"tests/reports/{timestamp}"
    os.makedirs(output_dir, exist_ok=True)
    parse = argparse.ArgumentParser(description="Getting the user config options")
    parse.add_argument("--runner",type=str,required=True,help="Runner option")
    parse.add_argument("--items", action="append", required=True,help="Multiple items as arguments (e.g., --processes 4 --testlevelsplit tests/testDemo.robot).")
    #parse.add_argument("--items",nargs="+",required=True,help="Runner config options")

    parse_arg = parse.parse_args()
    runner = parse_arg.runner

    config_data=["--outputdir",output_dir]
    try:
        for each_item in parse_arg.items[0].split(" "):
            if "_" in each_item:
                each_item = each_item.replace("_"," ")
            config_data.append(each_item)
        # config_data.extend([','.join(parse_arg.items[0].split(" "))])
    except Exception as ex:
        print(f"Invalid data :{str(ex)}")
        return

    if runner == "pabot":
        pabot_args = []
        pabot_args.extend(config_data[:-1])
        pabot_args.extend([
            "--output", "output.xml",
            "--log", "log.html",
            "--report", "report.html"])
        pabot_args.append(config_data[-1])
        print(pabot_args)
        pabot.main(pabot_args)

        # config_data.extend(pabot_args)
        # print(config_data)
        # pabot.main(config_data)








if __name__ == "__main__":
    main()

    # args={"outputdir":"reports/","processes":"4","path":"tests/","include":"smoke"}
    # args_after_update = pabot_arg_config(args)
    # print(args_after_update)
    # import os
    # print(os.getcwd())
    # print(os.path.exists("tests/testDemo1.robot"))
    # run_tests("pabot", [])
    # folder_path = run_tests("robot",[])
    # run_tests("rerun",folder_path)
