from .sessions import session_scope


def bulk_insert(engine, model, entries):
    with session_scope(engine) as session:
        session.bulk_insert_mappings(model, entries)
        session.commit()
