CREATE DATABASE attendance_db;

-- Connect to attendance_db before running below

CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE attendance (
    id SERIAL PRIMARY KEY,
    student_id INT REFERENCES students(id),
    class_date DATE NOT NULL,
    subject VARCHAR(100) NOT NULL,
    status VARCHAR(10) CHECK (status IN ('Present', 'Absent'))
);

INSERT INTO students (username, password, name)
VALUES ('student', 'student123', 'Dhakshan');

INSERT INTO attendance (student_id, class_date, subject, status)
VALUES
(1, '2026-10-01', 'Database Management', 'Present'),
(1, '2026-10-02', 'Data Structures', 'Present'),
(1, '2026-10-03', 'Computer Networks', 'Absent'),
(1, '2026-10-04', 'Java Programming', 'Present'),
(1, '2026-10-05', 'Software Engineering', 'Present');