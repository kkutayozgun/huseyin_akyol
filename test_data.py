#!/usr/bin/env python
class FreshTestData:
    @staticmethod
    def run():
        from page.models import (HomePageSeo, About, AboutList, Surgery, ChangeJourney, TreatmentPlan, TreatmentPlanItem, Image, Faq)

        HomePageSeo.objects.all().delete()
        About.objects.all().delete()
        Surgery.objects.all().delete()
        ChangeJourney.objects.all().delete()
        TreatmentPlan.objects.all().delete()
        Faq.objects.all().delete()
        TreatmentPlanItem.objects.all().delete()
        Image.objects.all().delete()

        test_img_dir = "assets/img"

        home = HomePageSeo.objects.create(
            title_intro="Peruvian further ampelitic",
            title="Banksian overcomplacency mistime",
            description="cutty communitary millwrighting evert imparipinnate metratonia tricarinate verjuice antitypically noncriminal aberdevine fleyland supracranial",
            bottom_content="Rouvillite phocid roughdress unkenneled Jennie Konstantinos acapnia debatement consentiently winterproof panelation restitution unmordanted Kylo porodite planispheric antifame",
        )
        home.slides.create(image=f"{test_img_dir}/1.jpg")
        home.slides.create(image=f"{test_img_dir}/3.jpg")
        home.slides.create(image=f"{test_img_dir}/4.jpg")

        about = About.objects.create(
            title="Banksian overcomplacency mistime benthonic",
            intro="Peruvian further ampelitic herbalist cartography haematoxylin unreformedness ammu exlex unequally Lychnis salangid lithotrity deposer faucalize plateiasmus deductively recountless antapocha penthiophene cerambycid hydrophyll intensifier flinthearted",
            description_title="Volcanoism silicate reset makeshiftiness autotractor",
            description="Rouvillite phocid roughdress unkenneled Jennie Konstantinos acapnia debatement consentiently winterproof panelation restitution unmordanted Kylo porodite planispheric antifame glaumrie astonisher drained kecksy epithecium classy herdswomanhydrosorbic",
        )
        aboutlist = about.aboutlist_set
        about_slides = about.slides
        about_slides_bottom = about.slides_bottom

        aboutlist.create(info="membraneless ventrocaudal cointersecting")
        aboutlist.create(info="emersed Izcateco pestiduct lulliloo")
        aboutlist.create(info="antiperistatically Cariamae pediment")
        aboutlist.create(info="postmeningeal brushy astart Nemalionales")
        aboutlist.create(info="batrachoplasty decaffeinize")
        aboutlist.create(info="unsuccess garageman spill")
        about_slides.create(image=f"{test_img_dir}/3.jpg")
        about_slides.create(image=f"{test_img_dir}/4.jpg")
        about_slides_bottom.create(image=f"{test_img_dir}/4.jpg")
        about_slides_bottom.create(image=f"{test_img_dir}/3.jpg")

        for _ in range(5):
            Surgery.objects.create(
               title="Homeopathic Humbug",
               description="regain clothesman devow semifasciated continuation nauseousness Bursera cassinette vaginoscopy doublehatching syntactically rougelike sciarid poachiness ctene bulbed encinillo",
               image=f"{test_img_dir}/5.jpg"
            )
            Surgery.objects.create(
               title="Postvenereal Cemental",
               description="multisector pyogenetic patera loosish afterwit unchangeableness mythometer shallowness schnauzer vencola volumetry ungenuine winful adlay Velika autoxeny Tatsanottine",
               image=f"{test_img_dir}/6.jpg"
            )
            Surgery.objects.create(
               title="Alternaria Praline",
               description="disembarrass Rephael affiliation biotome undiscounted imperil halcyonine amphore Alphean Davidic Homoneura Mandaean bisext branchiopulmonate helicoprotein pretannage unhoary",
               image=f"{test_img_dir}/7.jpg"
            )

        for _ in range(5):
            ChangeJourney.objects.create(image=f"{test_img_dir}/5.jpg")
            ChangeJourney.objects.create(image=f"{test_img_dir}/6.jpg")
            ChangeJourney.objects.create(image=f"{test_img_dir}/7.jpg")


        tp = TreatmentPlan.objects.create(name="Sulphoarsenious")
        tplist = tp.treatmentplanitem_set
        tplist.create(info="birimose lotiform himward")
        tplist.create(info="arteriorrhagia stearrhea Chickasaw")
        tplist.create(info="pinna calculable rococo")

        tp2 = TreatmentPlan.objects.create(name="Counterthwarting")
        tplist = tp2.treatmentplanitem_set
        tplist.create(info="birimose lotiform himward")
        tplist.create(info="arteriorrhagia stearrhea Chickasaw")
        tplist.create(info="pinna calculable rococo")
        tplist.create(info="aldamine Miniconjou quadragenarious")
        tplist.create(info="appropinquation che overflorid")


        for _ in range(2):
            Faq.objects.create(
               question="Overdistention serinette bloodripeness humblebee snozzle mobilianer?",
               answer="Disembarrass Rephael affiliation biotome undiscounted imperil halcyonine amphore Alphean Davidic Homoneura Mandaean bisext branchiopulmonate helicoprotein.",
            )
            Faq.objects.create(
               question="Gawn caving Watusi arthrempyesis Tortrix semisport lozenger unmistakingly?",
               answer="Mitigative vacationist capless declarative churlishness doublelunged scrapman choenix berther lingulid duologue slammocking committeewoman goatee pseudotrachea smokeless supinator apurpose spadicifloral uncrevassed Yahuna Pinnigrada undercarved sterilization",
            )
            Faq.objects.create(
               question="Trochleary physiopsychology oquassa cantor?",
               answer="periaster spearing bisinuate oppressiveness adunc speedy gluemaking acrawl quantify chilenite lactodensimeter soliloquium Shandy fairway homeochromatism palpiform archdevil Anastasian heelstrap hydatiform snowshed retraceable moonwalking Lemovices",
            )

FreshTestData.run()