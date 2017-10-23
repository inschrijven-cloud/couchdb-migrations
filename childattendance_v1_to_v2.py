import couchdb

URL='http://localhost:5984'
DBNAME = 'tenant-data-despeelberg-childattendance'

server = couchdb.Server(URL)
db = server[DBNAME]

v1 = db.view('_design/childattendance/_view/all')

for row in v1.rows:
    print(row.id)
    doc = db[row.id]
    if doc['kind'] == 'type/childattendance/v1':
        print('Doc is v1')
        doc['kind'] = 'type/childattendance/v2'
        
        if 'registeredTimeStamp' in doc['doc']:
            print('doc contains registeredTimeStamp')
            doc['doc']['arrived'] = doc['doc']['registeredTimeStamp']
            del doc['doc']['registeredTimeStamp']

        db.save(doc)

