

"""
Starting point of the application. This module is invoked from
the command line to run the analyses.
"""

import argparse
from contributor_activity_analysis import ContributorActivityAnalysis
import config
from example_analysis import ExampleAnalysis


def parse_args():
    """
    Parses the command line arguments that were provided along
    with the python command. The --feature flag must be provided as
    that determines what analysis to run. Optionally, you can pass in
    a user and/or a label to run analysis focusing on specific issues.
    
    You can also add more command line arguments following the pattern
    below.
    """
    ap = argparse.ArgumentParser("run.py")
    
    # Required parameter specifying what analysis to run
    ap.add_argument('--feature', '-f', type=int, required=True,
                    help='Which of the three features to run')
    
    # Optional parameter for analyses focusing on a specific user (i.e., contributor)
    ap.add_argument('--user', '-u', type=str, required=False,
                    help='Optional parameter for analyses focusing on a specific user')
    
    # Optional parameter for analyses focusing on a specific label
    ap.add_argument('--label', '-l', type=str, required=False,
                    help='Optional parameter for analyses focusing on a specific label')
    
    return ap.parse_args()



# Parse feature to call from command line arguments
args = parse_args()
# Add arguments to config so that they can be accessed in other parts of the application
config.overwrite_from_args(args)
contributor_analysis = ContributorActivityAnalysis()   
# Run the feature specified in the --feature flag
#Feature 0 graphs top 50 creators vs their # of issues
#Feature 1 prints in increasing order name of label and # of contributors associated
if args.feature == 0:
    ExampleAnalysis().run()
elif args.feature == 1:
    ExampleAnalysis().run1()
elif args.feature == 2:
    ExampleAnalysis().run2()
elif args.feature == 3:
    ExampleAnalysis().run3()
elif args.feature == 4:
    print("Running contributor activity analysis with focus on 'bug' issues...")
    contributor_analysis.run_contributor_analysis()
elif args.feature == 5:
    print("Running issue activity analysis by label...")
    contributor_analysis.analyze_issue_activity_by_label()
elif args.feature == 6:
    print(
        f"Running filtered activity analysis for {'user: ' + args.user if args.user else ''} "
        f"{'label: ' + args.label if args.label else ''}"
    )
    contributor_analysis.analyze_filtered_activity(user=args.user, label=args.label)
else:
    print('Need to specify which feature to run with --feature flag.')
