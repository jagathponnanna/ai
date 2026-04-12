import uuid
sessions={}

def get_or_create_session(session_id):
    if not session_id:
        session_id=str(uuid.uuid4())
        sessions[session_id]=[]
    return session_id,sessions.setdefault(session_id,[])