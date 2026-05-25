# ENDPOINTPULSE: Endpoint Threat Hunting Platform

Distributed endpoint event aggregation and behavioral threat hunting platform.

## Features

- Process, network, and file system event collection
- - Behavioral anomaly detection
  - - Suspicious process chain analysis
    - - Real-time threat hunting
      - - Multi-endpoint aggregation
        - - MITRE ATT&CK technique mapping
         
          - ## Quick Start
         
          - ```python
            from src.agent import EndpointAgent

            agent = EndpointAgent("endpoint-001")
            events = agent.aggregate_events()
            anomalies = agent.detect_anomalies(events)
            print(f"Collected {len(events)} events, found {len(anomalies)} anomalies")
            ```

            ## Architecture

            ```
            Endpoint Agents → Event Aggregator → Analyzer → Alert Engine
            ```

            ## Running Tests

            ```bash
            pytest tests/ -v --cov=src
            ```

            ## License

            MIT License
            
