var shuffleSequence = seq(
    "welcome",
    "intro",
    "startfam",
    sepWith("sep","practice"),
    "startexperiment",
    sepWith("sep", shuffle(randomize("test"), randomize("filler"))),
    "feedback"
);
var progressBarText = "Progress";
var practiceMessage = "Practice Session";
var completionMessage = "Your responses have been recorded. \r\nThank you for your participation.\r\n";

var defaults = [
    "Separator", {
        transfer: 1000,
        normalMessage: "Please wait for the next exchange."
    },
    "DashedSentence", {
        mode: "self-paced reading"
    },
    "AcceptabilityJudgment", {
        as: ["1", "2", "3", "4", "5", "6", "7"],
        presentAsScale: true,
        instructions: "Use number keys or click boxes to answer.",
        leftComment: "(Absolutely Unnatural)", rightComment: "(Perfectly Natural)"
    },
    "Question", {
        hasCorrect: true
    },
    "Message", {
        hideProgressBar: true
    },
    "Form", {
        hideProgressBar: true,
        continueOnReturn: true,
        saveReactionTime: false
    }
];

var items = [
    [
        "sep",
        "Separator",
        {}
    ],
    [
        "welcome",
        "Form",
        {
            html: { include: "welcome.html" }
        }
    ],
    [
        "intro",
        "Form",
        {
            html: { include: "intro.html" },
            validators: {
                age: function (s) { if (s.match(/^\d+$/)) return true; else return "Bad value for \u2018age\u2019";}
            }
        }
    ],
    [
        "startfam",
        "Form",
        {
            html: { include: "startfam.html" },
            validators: {
                age: function (s) { if (s.match(/^\d+$/)) return true; else return "Bad value for \u2018age\u2019";}
            }
        }
    ],
    [
        "startexperiment",
        "Form",
        {
            html: { include: "startexperiment.html" },
            validators: {
                age: function (s) { if (s.match(/^\d+$/)) return true; else return "Bad value for \u2018age\u2019";}
            }
        }
    ],
    [
        "feedback",
        "Form",
        {
            html: { include: "feedback.html" }
        }
    ],
    [
        "practice",
        "AcceptabilityJudgment",
        {s: {html: "<!--expo1XyzXpractice1-----------------><br><br>Margaret: Did you get your computer already fixed? <br> Gale: No, I'm waiting get my paycheck.<br> Margaret: Ok, because my brother said he can look at it if you want!"}}
    ],
    [
        "practice",
        "AcceptabilityJudgment",
        {s: {html: "<!--expo1XyzXpractice2-----------------><br><br>Ellen: Did I miss Cindy? <br> Sandra: Yes! Has already left, Cindy."}}
    ],
    [
        "practice",
        "AcceptabilityJudgment",
        {s: {html: "<!--expo1XyzXpractice3-----------------><br><br>Nicole: How’s your ankle doing?<br>Justin: It’s a lot better but I’m still limping around the house. No running for me for at least a week…"}}
    ],
    /*
    [
        ["test", 1],
        "AcceptabilityJudgment",
        {s: {html: "<div style=\"width: 50em;\"><!–– test_1_N_N––><p style=\"text-align: center;\">Sarah: Have you and Alex watched the last season of Stranger Things on Netflix? <br>Kelly: No but heard that it was totally crazy! <br>Sarah: I watched the whole thing in like two days because I had to know what happened…</p></div>"}}
    ],
    [
        ["test", 1],
        "AcceptabilityJudgment",
        {s: {html: "<div style=\"width: 50em;\"><!–– test_2_Y_Y––><p style=\"text-align: center;\">Sarah: Have you and Alex watched the last season of Stranger Things on Netflix?<br>Kelly: No but we heard that it was totally crazy! <br>Sarah: I watched the whole thing in like two days because I had to know what happened…</p></div>"}}
    ],
    [
        ["test", 2],
        "AcceptabilityJudgment",
        {s: {html: "<div style=\"width: 50em;\"><!–– test_2_N_Y––><p style=\"text-align: center;\">Edgar: Tomorrow will go to the gym, if you want to join.<br>Sam: Thanks but I can’t, I have plans already!</p></div>"}}
    ],
    [
        ["test", 2],
        "AcceptabilityJudgment",
        {s: {html: "<div style=\"width: 50em;\"><!–– test_1_Y_Y––><p style=\"text-align: center;\">Edgar: Tomorrow I will go to the gym, if you want to join. <br>Sam: Thanks but I can’t, I have plans already!</p></div>"}}
    ],
    [
        ["test", 3],
        "AcceptabilityJudgment",
        {s: {html: "<div style=\"width: 50em;\"><!–– test_1_N_N––><p style=\"text-align: center;\">Selene: Cannot believe haven’t sent your birthday card yet. It’s going to be late. <br>Mason: Haha no worries<br>Selene: I’m the worst friend ever! Sorry!</p></div>"}}
    ],
    */

// Begin experimental data input
    [["test", 1], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=1  pron=I  cond=a  cond_code=Rt.OV  attested=Y  ––><p style=\"text-align: center;\" hidden>Did you hear the new Taylor Swift album?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/1_1.png\" alt=\"Did you hear the new Taylor Swift album? Yes!  I can’t stop listening to it, it’s a problem!\" /></center></div>"}}],
    [["test", 1], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=1  pron=I  cond=b  cond_code=Rt.Null  attested=Y  ––><p style=\"text-align: center;\" hidden>Did you hear the new Taylor Swift album?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/1_2.png\" alt=\"Did you hear the new Taylor Swift album? Yes!  Can’t stop listening to it, it’s a problem!\" /></center></div>"}}],
    [["test", 1], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=1  pron=I  cond=c  cond_code=Embed.Ov  attested=Y  ––><p style=\"text-align: center;\" hidden>Did you hear the new Taylor Swift album?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/1_3.png\" alt=\"Did you hear the new Taylor Swift album? Yes!   I’ll admit that I can’t stop listening to it, it’s a problem!\" /></center></div>"}}],
    [["test", 1], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=1  pron=I  cond=d  cond_code=Embed.Null  attested=N  ––><p style=\"text-align: center;\" hidden>Did you hear the new Taylor Swift album?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/1_4.png\" alt=\"Did you hear the new Taylor Swift album? Yes!  I’ll admit that can’t stop listening to it, it’s a problem!\" /></center></div>"}}],
    [["test", 1], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=1  pron=I  cond=e  cond_code=Prepos.Ov  attested=Y  ––><p style=\"text-align: center;\" hidden>Did you hear the new Taylor Swift album?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/1_5.png\" alt=\"Did you hear the new Taylor Swift album? Yes!  It’s a problem, I can’t stop listening to it!\" /></center></div>"}}],
    [["test", 1], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=1  pron=I  cond=f  cond_code=Prepos.Null  attested=Y  ––><p style=\"text-align: center;\" hidden>Did you hear the new Taylor Swift album?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/1_6.png\" alt=\"Did you hear the new Taylor Swift album? Yes!  It’s a problem, can’t stop listening to it!\" /></center></div>"}}],
    [["test", 1], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=1  pron=YouSg  cond=g  cond_code=Rt2.OV  attested=Y  ––><p style=\"text-align: center;\" hidden>Did you hear the new Taylor Swift album?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/1_7.png\" alt=\"Did you hear the new Taylor Swift album? Yes!  If you listen to it once, you can’t stop listening to it!\" /></center></div>"}}],
    [["test", 1], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=1  pron=YouSg  cond=h  cond_code=Rt2.Null  attested=N  ––><p style=\"text-align: center;\" hidden>Did you hear the new Taylor Swift album?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/1_8.png\" alt=\"Did you hear the new Taylor Swift album? Yes!  If you listen to it once, can’t stop listening to it!\" /></center></div>"}}],
    [["test", 2], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=2  pron=We  cond=a  cond_code=Rt.OV  attested=Y  ––><p style=\"text-align: center;\" hidden>How did your basketball game go?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/2_2.png\" alt=\"How did your basketball game go? Yes!  We lost the game unfortunately... \" /></center></div>"}}],
    [["test", 2], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=2  pron=We  cond=b  cond_code=Rt.Null  attested=Y  ––><p style=\"text-align: center;\" hidden>How did your basketball game go?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/2_3.png\" alt=\"How did your basketball game go? Yes!  Lost the game unfortunately…\" /></center></div>"}}],
    [["test", 2], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=2  pron=We  cond=c  cond_code=Embed.Ov  attested=Y  ––><p style=\"text-align: center;\" hidden>How did your basketball game go?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/2_4.png\" alt=\"How did your basketball game go? Yes!  I’m sad to report that we lost the game…\" /></center></div>"}}],
    [["test", 2], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=2  pron=We  cond=d  cond_code=Embed.Null  attested=N  ––><p style=\"text-align: center;\" hidden>How did your basketball game go?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/2_5.png\" alt=\"How did your basketball game go? Yes!  I’m sad to report that lost the game…\" /></center></div>"}}],
    [["test", 2], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=2  pron=We  cond=e  cond_code=Prepos.Ov  attested=Y  ––><p style=\"text-align: center;\" hidden>How did your basketball game go?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/2_6.png\" alt=\"How did your basketball game go? Yes!  Unfortunately, we lost the game…\" /></center></div>"}}],
    [["test", 2], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=2  pron=We  cond=f  cond_code=Prepos.Null  attested=Y  ––><p style=\"text-align: center;\" hidden>How did your basketball game go?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/2_7.png\" alt=\"How did your basketball game go? Yes!  Unfortunately, lost the game…\" /></center></div>"}}],
    [["test", 2], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=2  pron=YouPl  cond=g  cond_code=Rt2.OV  attested=Y  ––><p style=\"text-align: center;\" hidden>Did you hear our bad news?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/2_8.png\" alt=\"Did you hear our bad news? Yes!  You guys lost your basketball game… I’m sorry!\" /></center></div>"}}],
    [["test", 2], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=2  pron=YouPl  cond=h  cond_code=Rt2.Null  attested=N  ––><p style=\"text-align: center;\" hidden>Did you hear our bad news?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/2_1.png\" alt=\"Did you hear our bad news? Yes!  Lost your basketball game… I’m sorry!\" /></center></div>"}}],
    [["test", 3], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=3  pron=She  cond=a  cond_code=Rt.OV  attested=Y  ––><p style=\"text-align: center;\" hidden>New York City is my new favorite city, it’s so lively!</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/3_3.png\" alt=\"New York City is my new favorite city, it’s so lively! Nice! Carly has a request for you. She wants you to buy her an “I love NY” shirt next time.\" /></center></div>"}}],
    [["test", 3], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=3  pron=She  cond=b  cond_code=Rt.Null  attested=Y  ––><p style=\"text-align: center;\" hidden>New York City is my new favorite city, it’s so lively!</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/3_4.png\" alt=\"New York City is my new favorite city, it’s so lively! Nice! Carly has a request for you. Wants you to buy her an “I love NY” shirt next time.\" /></center></div>"}}],
    [["test", 3], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=3  pron=She  cond=c  cond_code=Embed.Ov  attested=Y  ––><p style=\"text-align: center;\" hidden>New York City is my new favorite city, it’s so lively!</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/3_5.png\" alt=\"New York City is my new favorite city, it’s so lively! Nice! Carly has a request for you. She told me that she wants you to buy her an “I love NY” shirt next time.\" /></center></div>"}}],
    [["test", 3], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=3  pron=She  cond=d  cond_code=Embed.Null  attested=N  ––><p style=\"text-align: center;\" hidden>New York City is my new favorite city, it’s so lively!</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/3_6.png\" alt=\"New York City is my new favorite city, it’s so lively! Nice! Carly has a request for you. She told me that wants you to buy her an “I love NY” shirt next time.\" /></center></div>"}}],
    [["test", 3], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=3  pron=She  cond=e  cond_code=Prepos.Ov  attested=Y  ––><p style=\"text-align: center;\" hidden>New York City is my new favorite city, it’s so lively!</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/3_7.png\" alt=\"New York City is my new favorite city, it’s so lively! Nice! Carly has a request for you. Next time, she wants you to buy her an “I love NY” shirt.\" /></center></div>"}}],
    [["test", 3], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=3  pron=She  cond=f  cond_code=Prepos.Null  attested=Y  ––><p style=\"text-align: center;\" hidden>New York City is my new favorite city, it’s so lively!</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/3_8.png\" alt=\"New York City is my new favorite city, it’s so lively! Nice! Carly has a request for you. Next time, wants you to buy her an “I love NY” shirt.\" /></center></div>"}}],
    [["test", 3], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=3  pron=YouSg  cond=g  cond_code=Rt2.OV  attested=Y  ––><p style=\"text-align: center;\" hidden>Do you remember my request from your trip to New York City?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/3_1.png\" alt=\"Do you remember my request from your trip to New York City? Yes, you told me twice! You want me to buy you an “I love NY” shirt next time.\" /></center></div>"}}],
    [["test", 3], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=3  pron=YouSg  cond=h  cond_code=Rt2.Null  attested=N  ––><p style=\"text-align: center;\" hidden>Do you remember my request from your trip to New York City?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/3_2.png\" alt=\"Do you remember my request from your trip to New York City? Yes, you told me twice! Want me to buy you an “I love NY” shirt next time. \" /></center></div>"}}],
    [["test", 4], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=4  pron=They  cond=a  cond_code=Rt.OV  attested=Y  ––><p style=\"text-align: center;\" hidden>Ugh. I can’t get anything done when I’m at home. My parents cannot leave me alone.</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/4_4.png\" alt=\"Ugh. I can’t get anything done when I’m at home. My parents cannot leave me alone. It’s the same for me.  They wanted me to help them redecorate the living room yesterday!\" /></center></div>"}}],
    [["test", 4], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=4  pron=They  cond=b  cond_code=Rt.Null  attested=Y  ––><p style=\"text-align: center;\" hidden>Ugh. I can’t get anything done when I’m at home. My parents cannot leave me alone.</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/4_5.png\" alt=\"Ugh. I can’t get anything done when I’m at home. My parents cannot leave me alone. It’s the same for me.  Wanted me to help them redecorate the living room yesterday!\" /></center></div>"}}],
    [["test", 4], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=4  pron=They  cond=c  cond_code=Embed.Ov  attested=Y  ––><p style=\"text-align: center;\" hidden>Ugh. I can’t get anything done when I’m at home. My parents cannot leave me alone.</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/4_6.png\" alt=\"Ugh. I can’t get anything done when I’m at home. My parents cannot leave me alone. It’s the same for me.  I can’t believe that they wanted me to help them redecorate the living room yesterday!\" /></center></div>"}}],
    [["test", 4], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=4  pron=They  cond=d  cond_code=Embed.Null  attested=N  ––><p style=\"text-align: center;\" hidden>Ugh. I can’t get anything done when I’m at home. My parents cannot leave me alone.</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/4_7.png\" alt=\"Ugh. I can’t get anything done when I’m at home. My parents cannot leave me alone. It’s the same for me.  I can’t believe that wanted me to help them redecorate the living room yesterday!\" /></center></div>"}}],
    [["test", 4], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=4  pron=They  cond=e  cond_code=Prepos.Ov  attested=Y  ––><p style=\"text-align: center;\" hidden>Ugh. I can’t get anything done when I’m at home. My parents cannot leave me alone.</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/4_8.png\" alt=\"Ugh. I can’t get anything done when I’m at home. My parents cannot leave me alone. It’s the same for me.  Yesterday, they wanted me to help them redecorate the living room!\" /></center></div>"}}],
    [["test", 4], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=4  pron=They  cond=f  cond_code=Prepos.Null  attested=Y  ––><p style=\"text-align: center;\" hidden>Ugh. I can’t get anything done when I’m at home. My parents cannot leave me alone.</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/4_1.png\" alt=\"Ugh. I can’t get anything done when I’m at home. My parents cannot leave me alone. It’s the same for me.  Yesterday, wanted me to help them redecorate the living room!\" /></center></div>"}}],
    [["test", 4], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=4  pron=YouPl  cond=g  cond_code=Rt2.OV  attested=Y  ––><p style=\"text-align: center;\" hidden>Can you help us clean up the garden today?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/4_2.png\" alt=\"Can you help us clean up the garden today? Ugh. I can’t get anything done when I’m at home with you guys. You wanted me to help you redecorate the living room yesterday!\" /></center></div>"}}],
    [["test", 4], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=4  pron=YouPl  cond=h  cond_code=Rt2.Null  attested=N  ––><p style=\"text-align: center;\" hidden>Can you help us clean up the garden today?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/4_3.png\" alt=\"Can you help us clean up the garden today? Ugh. I can’t get anything done when I’m at home with you guys. Wanted me to help you redecorate the living room yesterday!\" /></center></div>"}}],
    [["test", 5], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=5  pron=I  cond=a  cond_code=Rt.OV  attested=Y  ––><p style=\"text-align: center;\" hidden>I woke up to the sound of my dog tearing apart my couch this morning. </p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/5_5.png\" alt=\"I woke up to the sound of my dog tearing apart my couch this morning.  Nooooo that dog is destroying your life. \" /></center></div>"}}],
    [["test", 5], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=5  pron=I  cond=b  cond_code=Rt.Null  attested=Y  ––><p style=\"text-align: center;\" hidden>Woke up to the sound of my dog tearing apart my couch this morning. </p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/5_6.png\" alt=\"Woke up to the sound of my dog tearing apart my couch this morning.  Nooooo that dog is destroying your life. \" /></center></div>"}}],
    [["test", 5], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=5  pron=I  cond=c  cond_code=Embed.Ov  attested=Y  ––><p style=\"text-align: center;\" hidden>I think that I woke up to the sound of my dog tearing apart my couch this morning.</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/5_7.png\" alt=\"I think that I woke up to the sound of my dog tearing apart my couch this morning. Nooooo that dog is destroying your life. \" /></center></div>"}}],
    [["test", 5], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=5  pron=I  cond=d  cond_code=Embed.Null  attested=N  ––><p style=\"text-align: center;\" hidden>I think that woke up to the sound of my dog tearing apart my couch this morning.</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/5_8.png\" alt=\"I think that woke up to the sound of my dog tearing apart my couch this morning. Nooooo that dog is destroying your life. \" /></center></div>"}}],
    [["test", 5], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=5  pron=I  cond=e  cond_code=Prepos.Ov  attested=Y  ––><p style=\"text-align: center;\" hidden>This morning I woke up to the sound of my dog tearing apart my couch. </p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/5_1.png\" alt=\"This morning I woke up to the sound of my dog tearing apart my couch.  Nooooo that dog is destroying your life. \" /></center></div>"}}],
    [["test", 5], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=5  pron=I  cond=f  cond_code=Prepos.Null  attested=Y  ––><p style=\"text-align: center;\" hidden>This morning woke up to the sound of my dog tearing apart my couch.</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/5_2.png\" alt=\"This morning woke up to the sound of my dog tearing apart my couch. Nooooo that dog is destroying your life. \" /></center></div>"}}],
    [["test", 5], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=5  pron=YouSg  cond=g  cond_code=Rt2.OV  attested=Y  ––><p style=\"text-align: center;\" hidden>So, you can’t go on vacation anymore and you have to pick up poop. You woke up to the sound of your dog tearing apart your couch this morning. Are you sure you made the right choice? lol</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/5_3.png\" alt=\"So, you can’t go on vacation anymore and you have to pick up poop. You woke up to the sound of your dog tearing apart your couch this morning. Are you sure you made the right choice? lol Honestly this dog is destroying my life. \" /></center></div>"}}],
    [["test", 5], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=5  pron=YouSg  cond=h  cond_code=Rt2.Null  attested=N  ––><p style=\"text-align: center;\" hidden>So, you can’t go on vacation anymore and you have to pick up poop. Woke up to the sound of your dog tearing apart your couch this morning. Are you sure you made the right choice? lol</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/5_4.png\" alt=\"So, you can’t go on vacation anymore and you have to pick up poop. Woke up to the sound of your dog tearing apart your couch this morning. Are you sure you made the right choice? lol Honestly this dog is destroying my life. \" /></center></div>"}}],
    [["test", 6], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=6  pron=We  cond=a  cond_code=Rt.OV  attested=Y  ––><p style=\"text-align: center;\" hidden>How was the rest of your Saturday?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/6_6.png\" alt=\"How was the rest of your Saturday? We had a nice dinner and then we went to see some live music after we saw the movie with you. \" /></center></div>"}}],
    [["test", 6], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=6  pron=We  cond=b  cond_code=Rt.Null  attested=Y  ––><p style=\"text-align: center;\" hidden>How was the rest of your Saturday?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/6_7.png\" alt=\"How was the rest of your Saturday? Had a nice dinner and then we went to see some live music after we saw the movie with you. \" /></center></div>"}}],
    [["test", 6], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=6  pron=We  cond=c  cond_code=Embed.Ov  attested=Y  ––><p style=\"text-align: center;\" hidden>How was the rest of your Saturday?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/6_8.png\" alt=\"How was the rest of your Saturday? We decided that we should have a nice dinner and then we went to see some live music after we saw the movie with you. \" /></center></div>"}}],
    [["test", 6], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=6  pron=We  cond=d  cond_code=Embed.Null  attested=N  ––><p style=\"text-align: center;\" hidden>How was the rest of your Saturday?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/6_1.png\" alt=\"How was the rest of your Saturday? We decided that should have a nice dinner and then we went to see some live music after we saw the movie with you. \" /></center></div>"}}],
    [["test", 6], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=6  pron=We  cond=e  cond_code=Prepos.Ov  attested=Y  ––><p style=\"text-align: center;\" hidden>How was the rest of your Saturday?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/6_2.png\" alt=\"How was the rest of your Saturday? After the movie, we had a nice dinner and then went to see some live music. \" /></center></div>"}}],
    [["test", 6], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=6  pron=We  cond=f  cond_code=Prepos.Null  attested=Y  ––><p style=\"text-align: center;\" hidden>How was the rest of your Saturday?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/6_3.png\" alt=\"How was the rest of your Saturday? After the movie, had a nice dinner and then went to see some live music. \" /></center></div>"}}],
    [["test", 6], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=6  pron=YouPl  cond=g  cond_code=Rt2.OV  attested=Y  ––><p style=\"text-align: center;\" hidden>How was the rest of your Saturday? You had a nice dinner, I know. But did you guys find any live music?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/6_4.png\" alt=\"How was the rest of your Saturday? You had a nice dinner, I know. But did you guys find any live music? Yeah, we found a band playing in a bar. \" /></center></div>"}}],
    [["test", 6], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=6  pron=YouPl  cond=h  cond_code=Rt2.Null  attested=N  ––><p style=\"text-align: center;\" hidden>How was the rest of your Saturday? Had a nice dinner, I know. But did you guys find any live music?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/6_5.png\" alt=\"How was the rest of your Saturday? Had a nice dinner, I know. But did you guys find any live music? Yeah, we found a band playing in a bar. \" /></center></div>"}}],
    [["test", 7], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=7  pron=He  cond=a  cond_code=Rt.OV  attested=Y  ––><p style=\"text-align: center;\" hidden>Will your dad drive us to the mall on Sunday?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/7_7.png\" alt=\"Will your dad drive us to the mall on Sunday? He can’t even though he promised that he would. \" /></center></div>"}}],
    [["test", 7], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=7  pron=He  cond=b  cond_code=Rt.Null  attested=Y  ––><p style=\"text-align: center;\" hidden>Will your dad drive us to the mall on Sunday?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/7_8.png\" alt=\"Will your dad drive us to the mall on Sunday? Can’t even though he promised that he would. \" /></center></div>"}}],
    [["test", 7], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=7  pron=He  cond=c  cond_code=Embed.Ov  attested=Y  ––><p style=\"text-align: center;\" hidden>Will your dad drive us to the mall on Sunday?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/7_1.png\" alt=\"Will your dad drive us to the mall on Sunday? He said that he can’t even though he promised that he would. \" /></center></div>"}}],
    [["test", 7], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=7  pron=He  cond=d  cond_code=Embed.Null  attested=N  ––><p style=\"text-align: center;\" hidden>Will your dad drive us to the mall on Sunday?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/7_2.png\" alt=\"Will your dad drive us to the mall on Sunday? He said that can’t even though he promised that he would. \" /></center></div>"}}],
    [["test", 7], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=7  pron=He  cond=e  cond_code=Prepos.Ov  attested=Y  ––><p style=\"text-align: center;\" hidden>Will your dad drive us to the mall on Sunday?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/7_3.png\" alt=\"Will your dad drive us to the mall on Sunday? Even though he promised he would, he can’t. \" /></center></div>"}}],
    [["test", 7], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=7  pron=He  cond=f  cond_code=Prepos.Null  attested=Y  ––><p style=\"text-align: center;\" hidden>Will your dad drive us to the mall on Sunday?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/7_4.png\" alt=\"Will your dad drive us to the mall on Sunday? Even though he promised he would, can’t. \" /></center></div>"}}],
    [["test", 7], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=7  pron=YouSg  cond=g  cond_code=Rt2.OV  attested=Y  ––><p style=\"text-align: center;\" hidden>Can I drive the kids to the mall on Sunday?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/7_5.png\" alt=\"Can I drive the kids to the mall on Sunday? You can’t because the car is still not working. \" /></center></div>"}}],
    [["test", 7], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=7  pron=YouSg  cond=h  cond_code=Rt2.Null  attested=N  ––><p style=\"text-align: center;\" hidden>Can I drive the kids to the mall on Sunday?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/7_6.png\" alt=\"Can I drive the kids to the mall on Sunday? Can’t because the car is still not working. \" /></center></div>"}}],
    [["test", 8], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=8  pron=They  cond=a  cond_code=Rt.OV  attested=Y  ––><p style=\"text-align: center;\" hidden>How are the kids doing?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/8_8.png\" alt=\"How are the kids doing? Great! We’re at the beach. They are building sandcastles, of course. I’ll send you a photo.\" /></center></div>"}}],
    [["test", 8], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=8  pron=They  cond=b  cond_code=Rt.Null  attested=Y  ––><p style=\"text-align: center;\" hidden>How are the kids doing?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/8_1.png\" alt=\"How are the kids doing? Great! We’re at the beach. Are building sandcastles, of course. I’ll send you a photo.\" /></center></div>"}}],
    [["test", 8], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=8  pron=They  cond=c  cond_code=Embed.Ov  attested=Y  ––><p style=\"text-align: center;\" hidden>How are the kids doing?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/8_2.png\" alt=\"How are the kids doing? Great! We’re at the beach, which means that they are building sandcastles of course. I’ll send you a photo.\" /></center></div>"}}],
    [["test", 8], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=8  pron=They  cond=d  cond_code=Embed.Null  attested=N  ––><p style=\"text-align: center;\" hidden>How are the kids doing?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/8_3.png\" alt=\"How are the kids doing? Great! We’re at the beach, which means that are building sandcastles of course. I’ll send you a photo.\" /></center></div>"}}],
    [["test", 8], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=8  pron=They  cond=e  cond_code=Prepos.Ov  attested=Y  ––><p style=\"text-align: center;\" hidden>How are the kids doing?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/8_4.png\" alt=\"How are the kids doing? Great! We’re at the beach.  So, of course they are building sandcastles. I’ll send you a photo.\" /></center></div>"}}],
    [["test", 8], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=8  pron=They  cond=f  cond_code=Prepos.Null  attested=Y  ––><p style=\"text-align: center;\" hidden>How are the kids doing?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/8_5.png\" alt=\"How are the kids doing? Great! We’re at the beach. So, of course are building sandcastles. I’ll send you a photo.\" /></center></div>"}}],
    [["test", 8], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=8  pron=YouPl  cond=g  cond_code=Rt2.OV  attested=Y  ––><p style=\"text-align: center;\" hidden>The kids are having a great time at the beach. Can you guess what we’re doing? I’ll send you a photo.</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/8_6.png\" alt=\"The kids are having a great time at the beach. Can you guess what we’re doing? I’ll send you a photo. You guys are building sandcastles, of course!  \" /></center></div>"}}],
    [["test", 8], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test  item_number=8  pron=YouPl  cond=h  cond_code=Rt2.Null  attested=N  ––><p style=\"text-align: center;\" hidden>The kids are having a great time at the beach. Can you guess what we’re doing? I’ll send you a photo.</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/8_7.png\" alt=\"The kids are having a great time at the beach. Can you guess what we’re doing? I’ll send you a photo. Are building sandcastles, of course! \" /></center></div>"}}],

];