from collections import defaultdict
from data_loader import DataLoader


class ContributorActivityAnalysis:
    def __init__(self):
        self.data_loader = DataLoader()
        self.contributor_activity = defaultdict(
            lambda: {
                "comments": 0,
                "labels": 0,
                "closures": 0,
                "reactions": 0,
                "other_events": 0,
            }
        )
        self.bug_label_activity = defaultdict(
            int
        )  # Track "bug" label activities per contributor

    def run_contributor_analysis(self):
        """Contributor activity analysis focusing on interaction with 'bug' issues."""
        issues = self.data_loader.get_issues()

        for issue in issues:
            is_bug_issue = "bug" in (label.lower() for label in issue.labels)

            for event in issue.events:
                author = event.author
                if not author:
                    continue

                # Track events based on their type
                if event.event_type == "comment":
                    self.contributor_activity[author]["comments"] += 1
                elif event.event_type == "label":
                    self.contributor_activity[author]["labels"] += 1
                elif event.event_type == "closed":
                    self.contributor_activity[author]["closures"] += 1
                elif event.event_type == "reaction":
                    self.contributor_activity[author]["reactions"] += 1
                else:
                    self.contributor_activity[author]["other_events"] += 1

                if is_bug_issue:
                    self.bug_label_activity[author] += 1

        self.display_top_contributors_with_bug_focus()

    def display_top_contributors_with_bug_focus(self):
        total_activity = {
            contributor: sum(events.values())
            for contributor, events in self.contributor_activity.items()
        }
        sorted_contributors = sorted(
            total_activity.items(), key=lambda item: item[1], reverse=True
        )[:5]

        print("Top Contributors by Activity and Focus on 'Bug' Issues:")
        for contributor, total_count in sorted_contributors:
            bug_count = self.bug_label_activity.get(contributor, 0)
            print(
                f"Contributor: {contributor}, Total Activity: {total_count}, 'Bug' Interactions: {bug_count}"
            )

    def analyze_issue_activity_by_label(self):
        """Analyzes which issue types are most active based on comments and contributor count."""
        label_activity = defaultdict(
            lambda: {"comment_count": 0, "unique_contributors": set()}
        )

        issues = self.data_loader.get_issues()
        for issue in issues:
            print(
                f"Issue Labels: {issue.labels}"
            )  # Print labels for each issue to check if they exist
            issue_labels = [label.lower() for label in issue.labels]

            for event in issue.events:
                print(
                    f"Event Type: {event.event_type}, Author: {event.author}"
                )  # Print event details
                if event.event_type == "comment" and event.author:
                    for label in issue_labels:
                        label_activity[label]["comment_count"] += 1
                        label_activity[label]["unique_contributors"].add(event.author)

        # Print out collected data to check if label activity is populated
        print("Collected label activity data:", label_activity)

        # Display results
        print("Issue Activity by Label:")
        for label, data in label_activity.items():
            print(
                f"Label: {label.capitalize()}, Comments: {data['comment_count']}, Unique Contributors: {len(data['unique_contributors'])}"
            )

    def analyze_filtered_activity(self, user=None, label=None):
        """Provides activity insights based on a specific user or label."""
        filtered_activity = defaultdict(
            lambda: {
                "comments": 0,
                "labels": 0,
                "closures": 0,
                "reactions": 0,
                "other_events": 0,
            }
        )

        issues = self.data_loader.get_issues()
        for issue in issues:
            if label and label.lower() not in (lbl.lower() for lbl in issue.labels):
                continue

            for event in issue.events:
                if user and event.author != user:
                    continue

                event_type = event.event_type
                if event.author:
                    if event_type == "comment":
                        filtered_activity[event.author]["comments"] += 1
                    elif event_type == "label":
                        filtered_activity[event.author]["labels"] += 1
                    elif event_type == "closed":
                        filtered_activity[event.author]["closures"] += 1
                    elif event_type == "reaction":
                        filtered_activity[event.author]["reactions"] += 1
                    else:
                        filtered_activity[event.author]["other_events"] += 1

        # Print results
        print(
            f"Filtered Activity for {'User: ' + user if user else ''}{' and ' if user and label else ''}{'Label: ' + label if label else ''}"
        )
        for contributor, activity in filtered_activity.items():
            print(f"Contributor: {contributor}, Activity: {activity}")
