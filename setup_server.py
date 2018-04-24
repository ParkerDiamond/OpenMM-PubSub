import os
import db

if __name__ == "__main__":
    db.db.create_all()
    os.mkdir('/tmp/openmm_jobs/')
