import os, sys
from azure.storage.blob import BlockBlobService
import pandas as pd
from scipy.stats import rankdata as rd
import xlwt, xlrd
import re
from flask import Flask, jsonify, request


results = {"result": "Input URL", "uploaded_url": ""}

app = Flask(__name__)

@app.route('/',methods=['GET'])
def test():
    return jsonify({'message': 'Your File has been Uploaded'})


@app.route('/process', methods=['POST'])
def process():

    data = request.get_json()

    url = data['url']

    pattern = re.compile(r'(?<=net\/).*?(?=\/)')
    match = pattern.findall(url)
    container_name = match[0]
    reg = r"(?<=" + container_name + "\/).*"
    pattern = re.compile(reg)
    match = pattern.findall(url)
    file_name1 = match[0]

    block_blob_service = BlockBlobService(account_name='dsconvreport',
                                          account_key='2wIt3xVY2HR5mXfl2489ctyE1CIewgwA0am+jE85HkOfOBKc7Af0KHHb2YS9Z466T+v9KClZXYeht21M3oXFYw==')

    full_path_to_file = file_name1[:-5] + "_downloaded.xlsx"

    block_blob_service.get_blob_to_path(container_name, file_name1, full_path_to_file)



    df = pd.read_excel(full_path_to_file)

    val = df.values.tolist()

    items = []
    supp_val = []
    ranks = []

    for i in val:
        if i[0] not in items:
            items.append(i[0])

    for j in items:
        for i in val:
            if i[0] == j:
                supp_val.append(i[2])
        ranks.extend(rd(supp_val, method='dense'))
        supp_val = []

    df['supplier_rank'] = ranks
    files = 'Test_Supplierdata_kundan.xlsx'
    df.to_excel(files)

    block_blob_service.create_blob_from_path(container_name, 'Test_Supplierdata_kundan.xlsx', 'Test_Supplierdata_kundan.xlsx')

    op_url ="https://dsconvreport.blob.core.windows.net/" + container_name + "/" + files
    results['result'] ="Congratulations, Your File has been Uploaded Successfully"
    results['uploaded_url'] = op_url

    return jsonify({'output_url': op_url, 'message': 'Your file has been downloaded and uploaded'})

if __name__=='__main__':
    app.run(debug=True, port=8080)



