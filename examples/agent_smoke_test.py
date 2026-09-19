"""Small deterministic smoke test for the AYORAI agent runtime."""

from ayorai.runtime import AyoraiRuntime


def main() -> None:
    runtime = AyoraiRuntime()

    result = runtime.run(
        "Research how RAG provenance can improve agent security",
        mode="research",
    )

    print(f"agent={result.agent}")
    print(f"risk={result.risk}")
    print(f"output={result.output}")
    print(f"audit_events={len(runtime.audit.events())}")


if __name__ == "__main__":
    main()
