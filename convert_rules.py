import json
import pprint

mz_rules_file = "easyList-blacklist.json"
mz_rules = json.load(open(mz_rules_file, "r"))

print(mz_rules["license"])
# pprint.pprint(mz_rules["categories"]["easyList"][0:10])
# print("total rules:", len(mz_rules["categories"]["easyList"]))

block_urls = []
for rule in mz_rules["categories"]["easyList"]:
    for key, val in rule.items():
        for website in val[key]:
            block_urls.append(website)

print("Found %d urls to block"% len(block_urls))
print("First 10 are:", ', '.join(block_urls[:10]))

new_ls_rules = {}
new_ls_rules["description"] = "Mirror of Mozilla easyList-blacklist.json from https://github.com/mozilla-services/shavar-prod-lists"
new_ls_rules["name"] = "Mozilla shavar easyList-blacklist Mirror"
new_ls_rules["rules"] = [{"action": "deny", "process":"any", "remote-domains": url} for url in block_urls]

json.dump(new_ls_rules, open("easyList-blacklist.lsrules", "w"))