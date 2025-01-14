python Runner.py --runner pabot --variable BROWSER:firefox --items "--processes 4 --testlevelsplit tests/testDemo1.robot"

python Runner.py --runner pabot --variable BROWSER:firefox --items "--processes 4 --test Check_whether_the_cart_is_displayed_in_the_home_page tests/testDemo1.robot"

python Runner.py --runner pabot --variable BROWSER:firefox --items "--processes 4 --include smoke tests/"


python Runner.py --runner pabot --variable BROWSER:firefox --items "--processes 4 --include smokeANDregression tests/"

python Runner.py --runner pabot --variable BROWSER:firefox --items "--processes 4 --include smokeORregression tests/"

python Runner.py --runner pabot --variable BROWSER:firefox --items "--processes 4 --exclude smoke tests/testDemo1.robot"

python Runner.py --runner pabot --variable BROWSER:firefox --items "--processes 4 --dryrun tests/"

##########################################################################################################
python Runner.py --runner robot --variable BROWSER:firefox --items "tests/testDemo3.robot"

python Runner.py --runner robot --variable BROWSER:firefox --items "--test Check_whether_the_cart_is_displayed_in_the_home_page tests/testDemo1.robot"

python Runner.py --runner robot --variable BROWSER:firefox --items "--include smoke tests/"

python Runner.py --runner robot --variable BROWSER:firefox --items "--include smokeANDregression tests/"

python Runner.py --runner robot --variable BROWSER:firefox --items "--include smokeORregression tests/"

python Runner.py --runner robot --variable BROWSER:firefox --items "--exclude smoke tests/testDemo1.robot"

python Runner.py --runner robot --variable BROWSER:firefox --items "--dryrun tests/"