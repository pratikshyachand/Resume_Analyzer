from project import read_job_description, compare, clean
import builtins

def test_read_job_description(monkeypatch):
    fake_input = iter(["Software Engineer", "Python required", "Remote", "EOF"])
    monkeypatch.setattr(builtins, "input", lambda: next(fake_input))
    result = read_job_description("Paste the job description and write EOF on a new line when done:")
    assert result == "Software Engineer\nPython required\nRemote"

def test_clean():
    assert clean("I love the Python!", stopword = True) == ['i', 'love', 'python']

def test_compare():
    assert compare("ReactJS, AngularJS, ExpressJS, NodeJS, jQuery, HTML, CSS","ReactJS, jQuery, HTML, CSS") == {"score":57.14, "missing":{'angularjs', 'expressjs', 'nodejs'}}
