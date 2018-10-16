from quart import Quart, request
from quart_cors import cors
from neo4j.v1 import GraphDatabase


app = Quart(__name__)
app = cors(app)


driver = GraphDatabase.driver(
            'bolt://0.0.0.0:7689',
            auth=('neo4j', 'K1r0ku'))


@app.route('/add-notes', methods=['POST'])
async def add_notes():
    """
    An async call serving POST requests from the frontend
    Each request handled is sent to Neo4j for possible modifications
    rtype -> None
    """

    def add_note(txn, note):
        return txn.run()

    async def write_to_db(note):
        with driver.session() as session:
            session.write_transaction(
                add_note,
                note )

    # def split_note_to_words(note):
    #     return note.split(" ")

    if request.method == 'POST':
        await write_to_db(request.get_data())


@app.route('/retrieve-notes', methods=['GET'])
async def retrieve_notes():

    def retrieve_notes(txn):
        return txn.run()

    async def retrieve_from_db():
        with driver.session() as session:
            session.write_transaction(
                retrieve_notes )

    if request.method == 'GET':
        await retrieve_from_db()