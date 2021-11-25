"""Buy some ram to some account."""


import eospyo

data = {
    "payer": "me.wam",
    "receiver": "me.wam",
    "quant": "5.00000000 WAX",
}

auth = eospyo.Authorization(actor="me.wam", permission="active")

action = eospyo.Action(
    account="eosio",
    name="buyram",
    data=data,
    authorization=[auth],
)

raw_transaction = eospyo.Transaction(actions=[action])

net = eospyo.WaxTestnet()
linked_transaction = raw_transaction.link(net=net)

key = "a_very_secret_key"
signed_transaction = linked_transaction.sign(key=key)

resp = signed_transaction.send()