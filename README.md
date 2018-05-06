## Very Basic DrugBank Parse

This is supposed to be used as an example for other people working with DrugBank on how to parse it, 
without the overhead of *really* understanding XML.

### What parse.py does

Call it like 

```
python3 parse.py --drugbankpath <Local Path to the DrugBank XML>
```

And it generates three files.

##### atc-agent.csv

All ATC code - Agent associations in the DrugBank DB.

##### atc-productname.csv

All ATC code - Productname associations in the DrugBank DB.

##### agent-productname.csv

All Agent - Productname associations in the DrugBank DB.

#### For SQL

This files can be used to feed DrugBank DB data easily into your SQL database.