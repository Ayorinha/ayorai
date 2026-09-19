from ayorai.memory.store import InMemoryStore


def test_memory_round_trip():
    memory = InMemoryStore()
    memory.put("task", "research")
    assert memory.get("task") == "research"
