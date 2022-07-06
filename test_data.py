#!/usr/bin/env python
import sys
import os
import django

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
django.setup()

from page.views import KVKKPage


class FreshTestData:
    @staticmethod
    def run():
        from page.models import (HomePageSeo, About, AboutList, Surgery, ChangeJourney, TreatmentPlan, TreatmentPlanItem, Image, Faq, KVKKPageSeo, CustomerReview)

        print("Deleting old content data...")
        HomePageSeo.objects.all().delete()
        About.objects.all().delete()
        Surgery.objects.all().delete()
        ChangeJourney.objects.all().delete()
        TreatmentPlan.objects.all().delete()
        Faq.objects.all().delete()
        TreatmentPlanItem.objects.all().delete()
        Image.objects.all().delete()
        KVKKPageSeo.objects.all().delete()
        CustomerReview.objects.all().delete()

        test_img_dir = "images"

        print("Inserting new test content...")
        home = HomePageSeo.objects.create(
            title_intro="Peruvian further ampelitic",
            title="Banksian overcomplacency mistime",
            description="Cutty communitary millwrighting evert imparipinnate metratonia tricarinate verjuice antitypically noncriminal aberdevine fleyland supracranial",
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

        kvkkpage = KVKKPageSeo.objects.create(content='<h1><span style="font-family:Comic Sans MS,cursive"><span style="font-size:18px">Lorem ipsum dolor sit amet,</span></span></h1>\r\n\r\n<p>consectetur adipiscing elit. Nam tincidunt arcu vel so<s>dales dictum. Nulla ut sodales magna. Prae</s>sent tellus erat, vestibulu<strong>m at hendrerit non, cursus id urna. Null</strong>am rhoncus sagittis porta. Suspendisse ut luctus sapien. Aliquam erat volutpat. Cras tincidunt lacus quis lobortis volutpat. Nulla facilisi. Donec orci libero, lacinia vehicula gravida eu, suscipit non mauris. Nulla facilisi. Curabitur facilisis ac ante vel placerat. Cras sodales, dolor nec ornare dignissim, felis magna commodo sem, non fringilla lacus metus eget urna. Suspendisse potenti.</p>\r\n\r\n<p>Mor<em>bi dapibus a urna et vestibulum. Fusce dapibus vestibu</em><u>lum libero, nec fringilla ipsum sceleri</u>sque tristique. Nunc at risus varius, dapibus nulla ac, aliquam mauris. Ut auctor dignissim ipsum sed pellentesque. In maximus faucibus ipsum. Nullam eget nisl eu nisl varius consectetur at non augue. Suspendisse <u>ut turpis vitae enim posuere facilisis. Donec molestie urna eget risus vulputate lobortis. Duis dapibus sed nulla bibendum tristique. Proin finibus congue purus. Interdum et mal</u>esuada fames ac ante ipsum primis in faucibus. Quisque quis dolor in nisi pharetra scelerisque. Nunc hendrerit, ipsum vitae tempor malesuada, nisl magna luctus elit, ac elementum tellus mauris sit amet mauris. Mauris elementum porttitor ante, vitae dignissim enim cursus quis.</p>\r\n\r\n<p>Maecenas mattis massa eget justo pulvinar blandit. Etiam molestie dolor ligula. Nulla ac enim elit. Donec at dignissim lacus. Quisque a mauris elit. Nulla vel laoreet lacus. Duis mattis tincidunt tortor ac viverra. Nam pretium neque diam, sed ultricies justo suscipit eu.</p>\r\n\r\n<p style="text-align:center">Etiam molestie dolor ligula. Nulla ac enim elit</p>\r\n\r\n<p>Phasellus pretium dictum magna, vitae consequat justo sollicitudin at. Quisque tellus ligula, eleifend ac facilisis vel, convallis sit amet dui. Quisque bibendum mi placerat, suscipit risus sit amet, vestibulum nunc. Donec sit amet suscipit libero. Phasellus lorem enim, ultrices vel dolor quis, eleifend convallis purus. Morbi eu magna aliquet magna pellentesque imperdiet. Mauris a dignissim diam. Aenean consequat ac leo in mattis. Quisque eleifend, tortor vitae tristique porttitor, mi leo tristique tortor, vel fringilla justo lorem sed odio. Donec iaculis erat convallis tincidunt tempus. Duis feugiat, orci ac facilisis pharetra, dui velit bibendum mauris, eget commodo tellus lacus et ex. Praesent rhoncus nec libero elementum molestie. Nam porttitor ipsum diam. Donec ornare augue quis quam vehicula, et pharetra nisl eleifend. Aenean bibendum justo id velit laoreet, vitae hendrerit libero sollicitudin.</p>\r\n\r\n<blockquote>\r\n<p>Vivamus scelerisque mi et vestibulum rutrum. Nulla at elit arcu. Morbi leo lectus, gravida id purus vel, vestibulum venenatis turpis. Curabitur lobortis diam sit amet ante malesuada, ut faucibus dui molestie. Suspendisse quis consectetur metus. Duis consequat metus libero, nec luctus ante faucibus at. Maecenas eleifend tortor libero, sit amet aliquet arcu lacinia id. Nulla convallis leo quis augue posuere, quis maximus enim volutpat. Aenean in sapien a nibh maximus placerat vitae sed dolor.</p>\r\n</blockquote>')

        CustomerReview.objects.create(
           full_name="Adriene Bachrach",
           job_title="Perennial unliveable",
           comment="Dijudicate paleornithology mannishly decadentism bantling floorless outgrowth developmentalist constructible impossible unreproached neuropterist ridiculous ureteroproctostomy unchristened roadability duopod misalienate unsubstantially mannie",
        )
        CustomerReview.objects.create(
           full_name="Christy Goyco",
           job_title="Gorgon nitrosulphate",
           comment="Galvanomagnet bachelorhood topcoating postscriptum bick egomaniac ruminative hiodont isograft renownful uncramp Pazend hemimellitene Pasteurelleae receptorial foreleech tragal bromoacetone warbling propitiatorily ogam ghost abaff involutorial",
        )
        CustomerReview.objects.create(
           full_name="Kali Collingsworth",
           job_title="Preseparate undrowned",
           comment="Stof interentanglement congratulant insuppressive bisexed astony apteral inimically photometrograph fanlike genista preharshness suffocative Alphonso nonorganization detectability refluxed metromaniacal",
        )
        print("Inserting test data completed!")

FreshTestData.run()