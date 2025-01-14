import argparse
import json
import os
import subprocess
from datetime import datetime
from pabot import pabot
from robot import run
from robot import run_cli
import xml.etree.ElementTree as ET

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
        "--variable", "BROWSER:firefox",
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

def check_failed_testcase(output_dir_xml):
    if not os.path.exists(output_dir_xml):
        print("File does not exist")
        return False,None
    cml_tree = ET.parse(output_dir_xml)
    root= cml_tree.getroot()

    statistics = root.find("statistics")

    if statistics is None:
        print("Unable to find statistics")
        return False,None
    failed_test_suite_name = []
    for each_stat in statistics.findall(".//stat"):
        if each_stat.get("fail") and int(each_stat.get("fail")) > 0:
            print("Fail Test case exist")
            if each_stat.get("name") not in failed_test_suite_name and each_stat.get("name") is not None and each_stat.get("name") != "Tests":
                failed_test_suite_name.append(each_stat.get("name"))
    if failed_test_suite_name is not None:
        return True,failed_test_suite_name
    else:
        return False,None




def main():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = f"tests/reports/{timestamp}"
    os.makedirs(output_dir, exist_ok=True)
    parse = argparse.ArgumentParser(description="Getting the user config options")
    parse.add_argument("--runner",type=str,required=True,help="Runner option")
    parse.add_argument("--variable",help="Browser details")
    parse.add_argument("--items", action="append", required=True,help="Multiple items as arguments (e.g., --processes 4 --testlevelsplit tests/testDemo.robot).")
    #parse.add_argument("--items",nargs="+",required=True,help="Runner config options")

    parse_arg = parse.parse_args()
    runner = parse_arg.runner

    config_data=["--outputdir",output_dir]
    try:
        for each_item in parse_arg.items[0].split(" "):
            if "_" in each_item:
                each_item = each_item.replace("_"," ")
            if each_item != '':
                config_data.append(each_item)
        # config_data.extend([','.join(parse_arg.items[0].split(" "))])
    except Exception as ex:
        print(f"Invalid data :{str(ex)}")
        return

    if runner == "pabot":
        pabot_args = ["pabot",]
        pabot_args.extend(config_data[:-1])
        pabot_args.extend([
            "--output", "output.xml",
            "--log", "log.html",
            "--report", "report.html",
            "--variable", parse_arg.variable])
        pabot_args.append(config_data[-1])
        print(pabot_args)
        try:
            process = subprocess.Popen(pabot_args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            process.terminate()
            process.wait()
            # return True
            # subprocess.run(pabot_args, check=True)
        except subprocess.CalledProcessError as ex:
            print(ex)
    elif runner == "robot":
        print(config_data)
        run_cli(config_data, exit=False)
    else:
        print("Invalid Runner option")
        return
    return runner, output_dir, config_data[-1]


        # config_data.extend(pabot_args)
        # print(config_data)
        # pabot.main(config_data)

def rerun(runner,output_dir,output_xml,rerun_output_dir,test_folder):
    log_path = os.path.join(output_dir, "rerun_log.html")
    report_path = os.path.join(output_dir, "rerun_report.html")
    if runner == 'robot':


        robot_args = [
            '--rerunfailed', output_xml,
            '--output', rerun_output_dir,
            "--log", log_path,
            "--report", report_path,
            test_folder
        ]
        run_cli(robot_args)



    elif runner == 'pabot':
        pabot_args = [
            '--rerunfailed', output_xml,
            "--outputdir", output_dir,
            '--output', 'rerun_output.xml',
            '--processes', '4',
            "--log", 'rerun_log.html',
            "--report", 'rerun_report.html',
            test_folder
        ]

        pabot.main(pabot_args)













if __name__ == "__main__":
    runner, output_dir, test_folder = main()
    if output_dir is not None:
        output_xml = os.path.join(output_dir, 'output.xml')
        # if runner == 'pabot':
        #     pabot_result_folder = os.path.join(output_dir,'pabot_results')
        #     output_xml = os.path.join(pabot_result_folder,'output.xml')
        # else:
        #     output_xml = os.path.join(output_dir,'output.xml')
        output_rerun_xml= None
        if runner == 'pabot':
            output_rerun_xml = os.path.join(output_dir, 'pabot_results', 'rerun_output.xml')
        else:
            output_rerun_xml = os.path.join(output_dir, 'rerun_output.xml')
        status,suite_name_list = check_failed_testcase(output_xml)
        if status:
            rerun(runner,output_dir,output_xml,output_rerun_xml,test_folder)




    # args={"outputdir":"reports/","processes":"4","path":"tests/","include":"smoke"}
    # args_after_update = pabot_arg_config(args)
    # print(args_after_update)
    # import os
    # print(os.getcwd())
    # print(os.path.exists("tests/testDemo1.robot"))
    # run_tests("pabot", [])
    # folder_path = run_tests("robot",[])
    # run_tests("rerun",folder_path)
