import psycopg2


def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="attendance_db",
        user="postgres",
        password="0462",
        port="5432"
    )


def login(username, password):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT id, name
        FROM students
        WHERE username = %s AND password = %s
        """,
        (username, password)
    )

    result = cur.fetchone()

    cur.close()
    conn.close()

    return result


def get_attendance(student_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT class_date, subject, status
        FROM attendance
        WHERE student_id = %s
        ORDER BY class_date
        """,
        (student_id,)
    )

    result = cur.fetchall()

    cur.close()
    conn.close()

    return result


def update_attendance(student_id, class_date, status):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE attendance
        SET status = %s
        WHERE student_id = %s
        AND class_date = %s
        """,
        (status, student_id, class_date)
    )

    conn.commit()

    cur.close()
    conn.close()