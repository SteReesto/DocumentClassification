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
	connection = connect()
	cursor = connection.cursor()

	query = "SELECT labels.id FROM labels WHERE labels.label = '" + label + "';"
	cursor.execute(query)

	row = cursor.fetchall()

	connection.commit()
	cursor.close()
	disconnect(connection)

	return str(row[0][0])


def create_document(object):
	connection = connect()
	cursor = connection.cursor()

	label_id = read_label_id(object['label'])

	query = "INSERT INTO documents VALUES (NULL, '" + object['filename'] + "', " + label_id + ");"
	cursor.execute(query)

	connection.commit()

	last_id = cursor.lastrowid

	cursor.close()
	disconnect(connection)

	return last_id


def create_label(label):
	try:
		connection = connect()
		cursor = connection.cursor()

		query = "INSERT INTO labels VALUES (NULL, '" + label + "');"

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

		query = "SELECT * FROM documents WHERE id = " + str(id) + ";"
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

		query = "SELECT * FROM labels WHERE id = " + str(id) + ";"
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

		query = "UPDATE documents SET filename = '" + object['filename'] + "', label_id = " + object['label_id'] + " WHERE id = " + str(object['id']) + ";"
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

		query = "DELETE FROM documents WHERE id = " + str(id) + ";"
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

		query = "DELETE FROM labels WHERE id = " + str(id) + ";"
		cursor.execute(query)

		connection.commit()

		return False

	except sqlite3.IntegrityError:
		return True

	finally:
		cursor.close()
		disconnect(connection)


def main():
	print(read_all_documents())
	print(read_all_labels())


if __name__ == '__main__':
	main()