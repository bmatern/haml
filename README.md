# HAML
HLA Antibody Markup Language - For antibody assay results and expert interpretation

## Version 0.1:

Started with HAMLCase_ver1_LG.xml (renamed to sample_file_haml_0_1.xml)

Generated XSD from XML using https://www.freeformatter.com/xsd-generator.html#ad-output

I like this XML generator because it doesn’t indent the XSD nearly as much.

This XSD has no restrictions.

xmllint --schema haml__version_0_1.xsd sample_file_haml_0_1.xml

sample_file_haml_0_1.xml validates

## Version 0.2:

XML Validation Error that was very difficult to fix:

xmllint --schema haml__version_0_2.xsd sample_file_haml_0_2.xml

haml__version_0_2.xsd:22: element sequence: Schemas parser error : Element '{http://www.w3.org/2001/XMLSchema}complexType': The content is not valid. Expected is (annotation?, (simpleContent | complexContent | ((group | all | choice | sequence)?, ((attribute | attributeGroup)*, anyAttribute?)))).

## Version 0.3:

Created by backfilling the restrictions of 0.2 into the previous haml.xsd.

xmllint --schema haml__version_0_3.xsd sample_file_haml_0_3.xml

sample_file_haml_0_3.xml validates

## Version 0.4:

Created by backfilling the restrictions of 0.4 into the previous haml.xsd.
Revisions from DaSH16 Hackathon and subsequent meetings
Addition of Assay Interpretation
Additional Working Sample data

xmllint --schema haml__version_0_4.xsd sample_file_haml_0_4.xml

sample_file_haml_0_4.xml validates

## Version 0.5:

Created by copying haml_version_0_4_4.xsd
### Changes
1. Restructuring of each HLA target test to include 9 individual bead results
* Working-Sample + Target-Test-Bead
* Working-Sample + Negative-Control-Bead
* Working-Sample + Positive-Control-Bead
* Negative-Control-Serum + Target-Test-Bead
* Negative-Control-Serum + Negative-Control-Bead
* Negative-Control-Serum + Positive-Control-Bead
* Positive-Control-Serum + Target-Test-Bead
* Positive-Control-Serum + Negative-Control-Bead
* Positive-Control-Serum + Positive-Control-Bead
2. Each bead MAY have raw_MFI scores, a declared adjustment formula and an adjusted_mfi score
3. The parent bead of each group MUST be the Working-Sample + Target-Test-Bead
4. The parent bead MUST have raw_MFI score, a declared formula and an adjusted_MFI score calculated from the target and negative-control scores of the 6 beads
5. Positive control results are only used to determine assay validity
6. Structural Changes
* Sample and working sample combined to follow FHIR Specimen and Specimen/Procedure model
* Negative-Control-Serum described as an independent Specimen to support standard reference from FHIR Observation model
* Positive-Control-Serum described as an independent Specimen to support standard reference from FHIR Observation model
* Assay Kit described as an independent Device to align with FHIR standard definitions
* Assay described as an independent Diagnostic Report to align with FHIR standard definitions

### To-Do's:
1. Elements supported by enumerated value sets to be described as 'extensible' allowing use of documented values or user-provided alternatives
2. Determine best way to represent 'extensible' values sets in XSD
3. Provide enumerated values for all declared enumerated types
4. Investigate representation of non-solid phase immunoassay assays

xmllint --schema haml__version_0_5.xsd sample_file_haml_0_5.xml

min_sample_file_haml_0_5.xml validates minimum required data for a compliant file
full_sample_file_haml_0_5.xml validates complete data for a compliant file 
