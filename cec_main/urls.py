from django.urls import path
from .views import *
urlpatterns=[
    path('',index,name='home'),
    path('about-aiml/',about_aiml,name='about-aiml'),
    path('about-ce/',about_ce,name='about-ce'),
    path('about-ece/',about_ece,name='about-ece'),
    path('about-ise/',about_ise,name='about-ise'),
    path('about-me/',about_me,name='about-me'),
    path('aboutus/',aboutus,name='aboutus'),
    path('achievers/',achievers,name='achievers'),
    path('activities-bs/',activities_bs,name='activities-bs'),
    path('activity-ce/',activity_ce,name='activity-ce'),
    path('activity-ise/',activity_ise,name='activity-ise'),
    path('activityme/',activityme,name='activityme'),
    path('adminstration/',adminstration,name='adminstration'),
    path('alumni/',alumni,name='alumni'),
    path('applicationform/',applicationform,name='applicationform'),
    path('bank/',bank,name='bank'),
    path('best-faculty/',best_faculty,name='best-faculty'),
    path('bridgecourse/',bridgecourse,name='bridgecourse'),
    path('bs-facilities/',bs_facilities,name='bs-facilities'),
    path('campusnews/',campusnews,name='campusnews'),
    path('cecabout-aiml/',cecabout_aiml,name='cecabout-aiml'),
    path('cecabout-ce/',cecabout_ce,name='cecabout-ce'),
    path('cecabout-ece/',cecabout_ece,name='cecabout-ece'),
    path('cecabout-ise/',cecabout_ise,name='cecabout-ise'),
    path('cecabout-me/',cecabout_me,name='cecabout-me'),
    path('cecaboutus/',cecaboutus,name='cecaboutus'),
    path('cecachievers/',cecachievers,name='cecachievers'),
    path('cecactivities-bs/',cecactivities_bs,name='cecactivities-bs'),
    path('cecactivity-ce/',cecactivity_ce,name='cecactivity-ce'),
    path('cecactivity-ise/',cecactivity_ise,name='cecactivity-ise'),
    path('cecactivityme/',cecactivityme,name='cecactivityme'),
    path('cecadminstration/',cecadminstration,name='cecadminstration'),
    path('cecalumni/',cecalumni,name='cecalumni'),
    path('cecapplicationform/',cecapplicationform,name='cecapplicationform'),
    path('cecbank/',cecbank,name='cecbank'),
    path('cecbest-faculty/',cecbest_faculty,name='cecbest-faculty'),
    path('cecbridgecourse/',cecbridgecourse,name='cecbridgecourse'),
    path('cecbs-facilities/',cecbs_facilities,name='cecbs-facilities'),
    path('ceccertificate/',ceccertificate,name='ceccertificate'),
    path('cecchairmanmsg/',cecchairmanmsg,name='cecchairmanmsg'),
    path('ceccoe/',ceccoe,name='ceccoe'),
    path('ceccommittees/',ceccommittees,name='ceccommittees'),
    path('ceccompany/',ceccompany,name='ceccompany'),
    path('ceccontact-us/',ceccontact_us,name='ceccontact-us'),
    path('ceccse-fa/',ceccse_fa,name='ceccse-fa'),
    path('ceccse-industry-interaction/',ceccse_industry_interaction,name='ceccse-industry-interaction'),
    path('ceccse-sa/',ceccse_sa,name='ceccse-sa'),
    path('ceccse-vison/',ceccse_vison,name='ceccse-vison'),
    path('ceccseptmreport/',ceccseptmreport,name='ceccseptmreport'),
    path('ceccultural-events/',ceccultural_events,name='ceccultural-events'),
    path('cecdepartment-be-ai-m/',cecdepartment_be_ai_m,name='cecdepartment-be-ai-m'),
    path('cecdepartment-civil-engineering/',cecdepartment_civil_engineering,name='cecdepartment-civil-engineering'),
    path('cecdepartment-computer-science-engineering/',cecdepartment_computer_science_engineering,name='cecdepartment-computer-science-engineering'),
    path('cecdepartment-electronics-communication-engineering/',cecdepartment_electronics_communication_engineering,name='cecdepartment-electronics-communication-engineering'),
    path('cecdepartment-mechanical-engineering/',cecdepartment_mechanical_engineering,name='cecdepartment-mechanical-engineering'),
    path('cecdepartment-ofbesic-science-fac/',cecdepartment_ofbesic_science_fac,name='cecdepartment-ofbesic-science-fac'),
    path('cecdepartment-ofbesic-science-humanity/',cecdepartment_ofbesic_science_humanity,name='cecdepartment-ofbesic-science-humanity'),
    path('cecdepartments/',cecdepartments,name='cecdepartments'),
    path('cecfacilities-ce/',cecfacilities_ce,name='cecfacilities-ce'),
    path('cecfacilities-ece/',cecfacilities_ece,name='cecfacilities-ece'),
    path('cecfacilities-me/',cecfacilities_me,name='cecfacilities-me'),
    path('cecfaculties-ceinfo/',cecfaculties_ceinfo,name='cecfaculties-ceinfo'),
    path('cecfaculties-eceinfo/',cecfaculties_eceinfo,name='cecfaculties-eceinfo'),
    path('cecfaculties-info-me/',cecfaculties_info_me,name='cecfaculties-info-me'),
    path('cecfaculties-iseinfo/',cecfaculties_iseinfo,name='cecfaculties-iseinfo'),
    path('cecfacultiesinfo-cse/',cecfacultiesinfo_cse,name='cecfacultiesinfo-cse'),
    path('cecfaculty-info-aiml/',cecfaculty_info_aiml,name='cecfaculty-info-aiml'),
    path('cecfaculty/',cecfaculty,name='cecfaculty'),
    path('cecgallery/',cecgallery,name='cecgallery'),
    path('cecgoveringcouncil/',cecgoveringcouncil,name='cecgoveringcouncil'),
    path('cecgrievance-portal/',cecgrievance_portal,name='cecgrievance-portal'),
    path('cechod-amil/',cechod_amil,name='cechod-amil'),
    path('cechod-bs/',cechod_bs,name='cechod-bs'),
    path('cechod-ce/',cechod_ce,name='cechod-ce'),
    path('cechod-cse/',cechod_cse,name='cechod-cse'),
    path('cechod-ece/',cechod_ece,name='cechod-ece'),
    path('cechod-me/',cechod_me,name='cechod-me'),
    path('cechodise/',cechodise,name='cechodise'),
    path('cechome/',cechome,name='cechome'),
    path('cecict/',cecict,name='cecict'),
    path('cecindex/',cecindex,name='cecindex'),
    path('cecindustry-partners/',cecindustry_partners,name='cecindustry-partners'),
    path('cecinformationscienceand-enginear/',cecinformationscienceand_enginear,name='cecinformationscienceand-enginear'),
    path('ceciqac/',ceciqac,name='ceciqac'),
    path('ceclanguage-lab/',ceclanguage_lab,name='ceclanguage-lab'),
    path('ceclibrary/',ceclibrary,name='ceclibrary'),
    path('ceclift/',ceclift,name='ceclift'),
    path('ceclistofcec/',ceclistofcec,name='ceclistofcec'),
    path('cecmagazine-cse/',cecmagazine_cse,name='cecmagazine-cse'),
    path('cecmagazine/',cecmagazine,name='cecmagazine'),
    path('cecmemberships/',cecmemberships,name='cecmemberships'),
    path('cecnaac/',cecnaac,name='cecnaac'),
    path('cecotherfacility/',cecotherfacility,name='cecotherfacility'),
    path('cecplaced-20-21/',cecplaced_20_21,name='cecplaced-20-21'),
    path('cecplaced-20-22/',cecplaced_20_22,name='cecplaced-20-22'),
    path('cecplacementdevelopments/',cecplacementdevelopments,name='cecplacementdevelopments'),
    path('cecplacementgoals/',cecplacementgoals,name='cecplacementgoals'),
    path('cecpotablewatersupply/',cecpotablewatersupply,name='cecpotablewatersupply'),
    path('cecprincipalmsg/',cecprincipalmsg,name='cecprincipalmsg'),
    path('cecprogramsoffers/',cecprogramsoffers,name='cecprogramsoffers'),
    path('cecprospectus/',cecprospectus,name='cecprospectus'),
    path('cecresearch-devlopment-cell/',cecresearch_devlopment_cell,name='cecresearch-devlopment-cell'),
    path('cecresearchcse-dept/',cecresearchcse_dept,name='cecresearchcse-dept'),
    path('cecsport/',cecsport,name='cecsport'),
    path('cecsports/',cecsports,name='cecsports'),
    path('cectransport/',cectransport,name='cectransport'),
    path('cecvehicleparking/',cecvehicleparking,name='cecvehicleparking'),
    path('cecvicechairmainmsg/',cecvicechairmainmsg,name='cecvicechairmainmsg'),
    path('cecvision-mission-aiml/',cecvision_mission_aiml,name='cecvision-mission-aiml'),
    path('cecvision-mission-ce/',cecvision_mission_ce,name='cecvision-mission-ce'),
    path('cecvision-mission-ece/',cecvision_mission_ece,name='cecvision-mission-ece'),
    path('cecvision-mission-me/',cecvision_mission_me,name='cecvision-mission-me'),
    path('cecvisionmision-ise/',cecvisionmision_ise,name='cecvisionmision-ise'),
    path('cecvisionmision/',cecvisionmision,name='cecvisionmision'),
    path('certificate/',certificate,name='certificate'),
    path('chairmanmsg/',chairmanmsg,name='chairmanmsg'),
    path('Clubtechactivities/',Clubtechactivities,name='Clubtechactivities'),
    path('coe/',coe,name='coe'),
    path('committees/',committees,name='committees'),
    path('company/',company,name='company'),
    path('contact-us/',contact_us,name='contact-us'),
    path('cse-fa/',cse_fa,name='cse-fa'),
    path('cse-industry-interaction/',cse_industry_interaction,name='cse-industry-interaction'),
    path('cse-sa/',cse_sa,name='cse-sa'),
    path('cse-vison/',cse_vison,name='cse-vison'),
    path('cseptmreport/',cseptmreport,name='cseptmreport'),
    path('cultural-events/',cultural_events,name='cultural-events'),
    path('de/',de,name='de'),
    path('department-be-ai-m/',department_be_ai_m,name='department-be-ai-m'),
    path('department-civil-engineering/',department_civil_engineering,name='department-civil-engineering'),
    path('department-computer-science-engineering/',department_computer_science_engineering,name='department-computer-science-engineering'),
    path('department-electronics-communication-engineering/',department_electronics_communication_engineering,name='department-electronics-communication-engineering'),
    path('department-mechanical-engineering/',department_mechanical_engineering,name='department-mechanical-engineering'),
    path('department-ofbesic-science-fac/',department_ofbesic_science_fac,name='department-ofbesic-science-fac'),
    path('department-ofbesic-science-humanity/',department_ofbesic_science_humanity,name='department-ofbesic-science-humanity'),
    path('departments/',departments,name='departments'),
    path('facilities-ce/',facilities_ce,name='facilities-ce'),
    path('facilities-ece/',facilities_ece,name='facilities-ece'),
    path('facilities-me/',facilities_me,name='facilities-me'),
    path('faculties-ceinfo/',faculties_ceinfo,name='faculties-ceinfo'),
    path('faculties-eceinfo/',faculties_eceinfo,name='faculties-eceinfo'),
    path('faculties-info-me/',faculties_info_me,name='faculties-info-me'),
    path('faculties-iseinfo/',faculties_iseinfo,name='faculties-iseinfo'),
    path('facultiesinfo-cse/',facultiesinfo_cse,name='facultiesinfo-cse'),
    path('faculty-info-aiml/',faculty_info_aiml,name='faculty-info-aiml'),
    path('faculty/',faculty,name='faculty'),
    path('gallery/',gallery,name='gallery'),
    path('goveringcouncil/',goveringcouncil,name='goveringcouncil'),
    path('grievance-portal/',grievance_portal,name='grievance-portal'),
    path('hod-amil/',hod_amil,name='hod-amil'),
    path('hod-bs/',hod_bs,name='hod-bs'),
    path('hod-ce/',hod_ce,name='hod-ce'),
    path('hod-cse/',hod_cse,name='hod-cse'),
    path('hod-ece/',hod_ece,name='hod-ece'),
    path('hod-me/',hod_me,name='hod-me'),
    path('hodise/',hodise,name='hodise'),
    path('ict/',ict,name='ict'),
    path('index/',index,name='index'),
    path('industry-partners/',industry_partners,name='industry-partners'),
    path('informationscienceand-enginear/',informationscienceand_enginear,name='informationscienceand-enginear'),
    path('iqac/',iqac,name='iqac'),
    path('language-lab/',language_lab,name='language-lab'),
    path('library/',library,name='library'),
    path('lift/',lift,name='lift'),
    path('listofcec/',listofcec,name='listofcec'),
    path('magazine-cse/',magazine_cse,name='magazine-cse'),
    path('magazine/',magazine,name='magazine'),
    path('memberships/',memberships,name='memberships'),
    path('naac/',naac,name='naac'),
    path('otherfacility/',otherfacility,name='otherfacility'),
    path('placed-20-21/',placed_20_21,name='placed-20-21'),
    path('placed-20-22/',placed_20_22,name='placed-20-22'),
    path('placementdevelopments/',placementdevelopments,name='placementdevelopments'),
    path('placementgoals/',placementgoals,name='placementgoals'),
    path('potablewatersupply/',potablewatersupply,name='potablewatersupply'),
    path('principalmsg/',principalmsg,name='principalmsg'),
    path('programsoffers/',programsoffers,name='programsoffers'),
    path('prospectus/',prospectus,name='prospectus'),
    path('research-devlopment-cell/',research_devlopment_cell,name='research-devlopment-cell'),
    path('researchcse-dept/',researchcse_dept,name='researchcse-dept'),
    path('sport/',sport,name='sport'),
    path('sports/',sports,name='sports'),
    path('transport/',transport,name='transport'),
    path('vehicleparking/',vehicleparking,name='vehicleparking'),
    path('vicechairmainmsg/',vicechairmainmsg,name='vicechairmainmsg'),
    path('vision-mission-aiml/',vision_mission_aiml,name='vision-mission-aiml'),
    path('vision-mission-ce/',vision_mission_ce,name='vision-mission-ce'),
    path('vision-mission-ece/',vision_mission_ece,name='vision-mission-ece'),
    path('vision-mission-me/',vision_mission_me,name='vision-mission-me'),
    path('visionmision-ise/',visionmision_ise,name='visionmision-ise'),
    path('visionmision/',visionmision,name='visionmision'),
]