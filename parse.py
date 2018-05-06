from tqdm import tqdm
import lxml.etree as ET
from itertools import chain, product
import csv
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--drugbankpath', type=str,
                    help='Set this to the path of your drugbank XML.')

args = parser.parse_args()

tree = ET.parse(args.drugbankpath)
print("parse of drugbank done")

root = tree.getroot()

ns = {'db': 'http://www.drugbank.ca'}

with open('atc-agent.csv', 'w') as atc_agent,\
        open('atc-productname.csv', 'w') as atc_product,\
        open('agent-productname.csv', 'w') as agent_product:
    atc_agent_writer = csv.writer(atc_agent)
    atc_product_writer = csv.writer(atc_product)
    agent_product_writer = csv.writer(agent_product)

    for drug in tqdm(tree.xpath("db:drug[db:groups/db:group='approved']", namespaces=ns)):

        drugName = drug.find("db:name", ns).text
        agent_synonyms = map(lambda x: x.text, drug.findall(
            "db:synonyms/db:synonym", ns))
        agent_synonyms = list(set(list(agent_synonyms) + [drugName]))

        product_names = map(
            lambda x: x.text, drug.findall("db:products/db:product/db:name", ns))
        product_names = chain(product_names, map(lambda x: x.text, drug.findall(
            "db:international-brands/db:international-brand/db:name", ns)))
        product_names = list(set(product_names))

        codes = drug.findall("db:atc-codes/db:atc-code", ns)
        atcs = list(set([code.get("code") for code in codes]))

        atc_agent_writer.writerows(product(atcs, agent_synonyms))
        atc_product_writer.writerows(product(atcs, product_names))
        agent_product_writer.writerows(
            product(agent_synonyms, product_names))
