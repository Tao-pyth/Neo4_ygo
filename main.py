from neo4j import GraphDatabase

# ✅ routing回避（直結）
URI = "bolt+ssc://d94d8f7e.databases.neo4j.io:7687"
USER = "neo4j"
PASSWORD = "0pzR4chdsjrgOiWGQSwYbxSQRDTXILnUGdoUKbY5xY0"

def main():
    driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))
    driver.verify_connectivity()  # ここで接続確認

    # AuraはDB名が neo4j のことが多いので明示（効くケースがあります）
    with driver.session(database="neo4j") as session:
        value = session.run("RETURN 1 AS n").single()["n"]
        print("Connected:", value)

    driver.close()

if __name__ == "__main__":
    main()
