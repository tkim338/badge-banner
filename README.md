# badge-banner

## Tool to enforce badge access policies in restricted areas

Uses security camera footage and badge scan event data to flag badge scan events that are used by multiple people.  This
includes one badge scan event that allows in many people or multiple scans of the same badge to allow in multiple 
people.

Uses Amazon Rekognition's person pathing feature to identify unique persons. 