"""Endpoint Agent"""

import json
from typing import List, Dict


class EndpointAgent:
      """Collects telemetry from endpoints"""

    def __init__(self, endpoint_id: str):
              self.endpoint_id = endpoint_id
              self.events = []

    def collect_process_events(self) -> List[Dict]:
              """Collect process execution events"""
              return [
                  {'type': 'process_execution', 'name': 'powershell.exe', 'parent': 'explorer.exe'},
                  {'type': 'process_execution', 'name': 'cmd.exe', 'parent': 'svchost.exe'},
              ]

    def collect_network_events(self) -> List[Dict]:
              """Collect network connection events"""
              return [
                  {'type': 'network_connection', 'source': '192.168.1.100', 'destination': '8.8.8.8'},
                  {'type': 'dns_query', 'domain': 'malicious-c2.com'},
              ]

    def collect_file_events(self) -> List[Dict]:
              """Collect file system events"""
              return [
                  {'type': 'file_created', 'path': 'C:\\Windows\\Temp\\payload.exe'},
              ]

    def aggregate_events(self) -> List[Dict]:
              """Aggregate all events"""
              all_events = []
              all_events.extend(self.collect_process_events())
              all_events.extend(self.collect_network_events())
              all_events.extend(self.collect_file_events())
              return all_events

    def detect_anomalies(self, events: List[Dict]) -> List[Dict]:
              """Detect behavioral anomalies"""
              anomalies = []
              suspicious = ['powershell.exe', 'cmd.exe', 'wscript.exe']
              for event in events:
                            if event.get('type') == 'process_execution':
                                              if event.get('name') in suspicious:
                                                                    anomalies.append({
                                                                                              'type': 'suspicious_process',
                                                                                              'process': event['name'],
                                                                                              'severity': 'MEDIUM'
                                                                    })
                                                        return anomalies


if __name__ == "__main__":
      agent = EndpointAgent("endpoint-001")
      events = agent.aggregate_events()
      print(json.dumps(events, indent=2))
  
