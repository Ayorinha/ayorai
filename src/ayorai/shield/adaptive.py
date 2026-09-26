from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class ThreatObservation:
    source: str
    signal: str
    evidence_hash: str
    confidence: float


@dataclass(frozen=True)
class RuleCandidate:
    rule_id: str
    observation: ThreatObservation
    rationale: str
    status: str = "quarantined"


class AdaptiveDefense:
    """Safe learning loop: observations may propose rules, but never self-promote.

    The internet, threat feeds, models and telemetry are treated as untrusted
    evidence. A candidate rule must pass deterministic validation and an explicit
    promotion policy before it can affect enforcement.
    """

    def __init__(self, validator: Callable[[RuleCandidate], bool] | None = None) -> None:
        self._validator = validator or (lambda candidate: candidate.observation.confidence >= 0.95)
        self._candidates: list[RuleCandidate] = []
        self._active_rules: dict[str, RuleCandidate] = {}

    def observe(self, observation: ThreatObservation, *, rule_id: str, rationale: str) -> RuleCandidate:
        candidate = RuleCandidate(rule_id, observation, rationale)
        self._candidates.append(candidate)
        return candidate

    def validate(self, candidate: RuleCandidate) -> RuleCandidate:
        if candidate not in self._candidates:
            raise ValueError("Unknown threat candidate")
        if not self._validator(candidate):
            return RuleCandidate(candidate.rule_id, candidate.observation, candidate.rationale, "rejected")
        return RuleCandidate(candidate.rule_id, candidate.observation, candidate.rationale, "validated")

    def promote(self, candidate: RuleCandidate) -> RuleCandidate:
        validated = self.validate(candidate)
        if validated.status != "validated":
            raise ValueError("Only validated rules can be promoted")
        self._active_rules[validated.rule_id] = validated
        return RuleCandidate(validated.rule_id, validated.observation, validated.rationale, "active")

    def candidates(self) -> tuple[RuleCandidate, ...]:
        return tuple(self._candidates)

    def active_rules(self) -> tuple[RuleCandidate, ...]:
        return tuple(self._active_rules.values())
