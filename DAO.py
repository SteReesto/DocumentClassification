import sqlite3


def connect():
	return sqlite3.connect('DB/documentClassification.db')


def disconnect(connection):
	connection.close()


def read_all_documents():
	connection = connect()
	cursor = connection.cursor()

	query = "SELECT * FROM documents;"
	cursor.execute(query)

	rows = cursor.fetchall()

	connection.commit()
	cursor.close()
	disconnect(connection)

	return rows


def read_all_labels():
	connection = connect()
	cursor = connection.cursor()

	query = "SELECT * FROM labels;"
	cursor.execute(query)

	rows = cursor.fetchall()

	connection.commit()
	cursor.close()
	disconnect(connection)

	return rows


def read_label_id(label):
	try:
		connection = connect()
		cursor = connection.cursor()

		query = f"SELECT labels.id FROM labels WHERE labels.label = '{label}';"
		cursor.execute(query)
		row = cursor.fetchall()
		connection.commit()

		return str(row[0][0])

	except Exception as e:
		return None

	finally:
		cursor.close()
		disconnect(connection)


def create_document(object):
	try:
		connection = connect()
		cursor = connection.cursor()

		label_id = read_label_id(object['label'])

		if label_id is None:
			create_label(object['label'])
			label_id = read_label_id(object['label'])

		query = f"INSERT INTO documents VALUES (NULL, '{object['filename']}', {label_id});"
		cursor.execute(query)
		last_id = cursor.lastrowid
		connection.commit()

		return last_id

	except Exception as e:
		return None

	finally:
		cursor.close()
		disconnect(connection)


def create_label(label):
	try:
		connection = connect()
		cursor = connection.cursor()

		query = f"INSERT INTO labels VALUES (NULL, '{label}');"

		cursor.execute(query)
		connection.commit()

		return False

	except sqlite3.IntegrityError:
		return True

	finally:
		cursor.close()
		disconnect(connection)


def read_document(id):
	try:
		connection = connect()
		cursor = connection.cursor()

		query = f"SELECT * FROM documents WHERE id = {str(id)};"
		cursor.execute(query)

		row = cursor.fetchall()

		connection.commit()

		return row

	except sqlite3.IntegrityError:
		return None

	finally:
		cursor.close()
		disconnect(connection)


def read_label(id):
	try:
		connection = connect()
		cursor = connection.cursor()

		query = f"SELECT * FROM labels WHERE id = {str(id)};"
		cursor.execute(query)

		row = cursor.fetchall()

		connection.commit()

		return row

	except sqlite3.IntegrityError:
		return None

	finally:
		cursor.close()
		disconnect(connection)


def update_document(object):
	try:
		connection = connect()
		cursor = connection.cursor()

		query = f"UPDATE documents SET filename = '{object['filename']}', label_id = {object['label_id']} WHERE id = {str(object['id'])};"
		cursor.execute(query)

		row = cursor.fetchall()

		connection.commit()

		return row

	except sqlite3.IntegrityError:
		return None

	finally:
		cursor.close()
		disconnect(connection)


def delete_document(id):
	try:
		connection = connect()
		cursor = connection.cursor()

		query = f"DELETE FROM documents WHERE id = {str(id)};"
		cursor.execute(query)

		connection.commit()

		return False

	except sqlite3.IntegrityError:
		return True

	finally:
		cursor.close()
		disconnect(connection)


def delete_label(id):
	try:
		connection = connect()
		cursor = connection.cursor()

		query = f"DELETE FROM labels WHERE id = {str(id)};"
		cursor.execute(query)

		connection.commit()

		return False

	except sqlite3.IntegrityError:
		return True

	finally:
		cursor.close()
		disconnect(connection)
