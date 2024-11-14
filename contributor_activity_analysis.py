from collections import defaultdict
from data_loader import DataLoader
import pandas as pd
import matplotlib.pyplot as plt


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


    def visualize_issue_activity(self):
        """Visualizes the number of issues created over time and per year in one plot with two graphs."""
        # Load issues data
        issues = self.data_loader.get_issues()

        # Initialize label counts
        label_counts = defaultdict(lambda: defaultdict(int))

        # Extract created_date and labels from issues
        events_data = pd.DataFrame({
            'created_date': [issue.created_date for issue in issues],
            'labels': [issue.labels for issue in issues]
        })
        
        # Convert created_date to datetime
        events_data['created_date'] = pd.to_datetime(events_data['created_date'])

        # Calculate top 3 labels per year
        for _, row in events_data.iterrows():
            year = row['created_date'].year
            for label in row['labels']:
                label_counts[year][label] += 1

        # Sort and get top 3 labels for each year
        top_labels_per_year = {
            year: sorted(counts.items(), key=lambda x: x[1], reverse=True)[:3]
            for year, counts in label_counts.items()
        }

        # Prepare data for visualization
        years = sorted(top_labels_per_year.keys())
        
        # Prepare data for stacked bar plot
        labels_per_year = {year: [label for label, _ in top_labels] for year, top_labels in top_labels_per_year.items()}
        counts_per_year = {year: [count for _, count in top_labels] for year, top_labels in top_labels_per_year.items()}

        # Create a figure and axis
        fig, ax = plt.subplots(figsize=(12, 8))

        # Plotting the top 3 labels per year as stacked bars
        bottom = [0] * len(years)  # Initialize bottom of bars to zero
        colors = ['#ff9999','#66b3ff','#99ff99']  # Colors for the three labels

        for i in range(3):  # We know we're plotting only the top 3 labels per year
            values = [counts_per_year[year][i] if i < len(counts_per_year[year]) else 0 for year in years]
            ax.bar(years, values, bottom=bottom, color=colors[i], label=f'Label {i+1}')
            bottom = [sum(x) for x in zip(bottom, values)]  # Update bottom to stack bars

        # Set axis titles and legend
        ax.set_title('Top 3 Labels Count for Each Year')
        ax.set_xlabel('Year')
        ax.set_ylabel('Count')
        
        # Create a custom legend with actual label names
        handles, _ = ax.get_legend_handles_labels()
        
        legend_labels = []
        
        for i in range(3):
            legend_label = ', '.join([labels_per_year[year][i] if i < len(labels_per_year[year]) else '' for year in years])
            legend_labels.append(legend_label)
        
        ax.legend(handles, legend_labels, title='Top Labels', bbox_to_anchor=(1.05, 1), loc='upper left')

        plt.tight_layout()
        plt.show()



