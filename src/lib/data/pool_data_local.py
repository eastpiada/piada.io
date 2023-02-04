import koios_python
import json
import pandas as pd
from dotenv import load_dotenv
#from github import Github
load_dotenv()
import os

# Get our github api key from the file .env
# Then check login to github

#personal_access_token = os.getenv('PIADA_TOKEN')
# using an access token
#g = Github(personal_access_token)

# Check that we can access the github api and returns correct user
#try:   
#    user = g.get_user()
#    print(user.name)
#except ApiError as e:
#    print(e)

# create a koios_python instance and set the network
kp = koios_python.URLs(network='mainnet')

# get tip and make into a dataframe
tip = pd.DataFrame(kp.get_tip(), index=[0])

# get current epoch number
epoch = tip.epoch_no[0]

# Pool_bech32_ID
piada = 'pool1hrv8gtrm0dgjg6zyss5uwa4nkruzfnh5vrdkr2sayj7x2nw6mjc'

piada_history = pd.DataFrame(kp.get_pool_history(piada))

piada_info = pd.DataFrame(kp.get_pool_info(piada))

# Need pledge, live stake, live delegators, margin, block count, past 10 epoch ros, epoch_current then put it into a json file
pledge = round(int(piada_info.pledge[0])/1000000)
total_delegated = round(int(piada_info.live_stake[0])/1000000)
number_of_delegators = int(piada_info.live_delegators[0])
pool_fee = piada_info.margin[0] * 100
block_count = int(piada_info.block_count[0])
epoch = int(tip.epoch_no[0])
delegate_rewards = round((piada_history.deleg_rewards.astype(int) / 1000000).sum())
ten_epoch_ros = round(piada_history.epoch_ros[0:9].mean(), 2)

# lets make the some of the numbers look nice and convert to strings to look like this "80,000" without the ending .0
pledge = "{:,}".format(pledge)
delegate_rewards = "{:,}".format(delegate_rewards)
total_delegated = "{:,}".format(total_delegated)

# now lets get all this data above into a dictionary with keys as variable names and values as the variable values
pool_data = dict(pledge=pledge, total_delegated=total_delegated, number_of_delegators=number_of_delegators, pool_fee=pool_fee, block_count=block_count, epoch=epoch, delegate_rewards=delegate_rewards, ten_epoch_ros=ten_epoch_ros)

# now lets convert the dictionary to a json file
pool_data_json = json.dumps(pool_data)
print(pool_data_json)

#repo = "eastpiada/eastpiada.github.io"
path = "src/lib/data/poolData.json"


#repo = g.get_repo(repo)
#sha = repo.get_contents(path).sha
#update_data = repo.update_file(
#    path = path, 
#    message = "add new file", 
#    content = pool_data_json, 
#    branch = "master",
#    sha=sha
#)
#print(update_data)
