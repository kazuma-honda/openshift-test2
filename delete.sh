#!/bin/bash
oc delete route --all
oc delete svc --all
oc delete dc --all
oc delete bc --all
oc delete is --all
oc delete deployment --all

oc delete pod --all

oc get all
