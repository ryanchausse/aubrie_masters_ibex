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

// Begin experiment data: 
[["test", 1], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=1 pron=I cond=a cond_code=Rt.OV attested=Y ––><p style=\"text-align: center;\" hidden>Did you hear the new Taylor Swift album?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/1_1.png\" alt=\"Did you hear the new Taylor Swift album? Yeah! I love listening to it while I’m at work!\"/></center></div>"}}],
[["test", 1], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=1 pron=I cond=b cond_code=Rt.Null attested=Y ––><p style=\"text-align: center;\" hidden>Did you hear the new Taylor Swift album?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/1_2.png\" alt=\"Did you hear the new Taylor Swift album? Yeah! Love listening to it while I’m at work!\"/></center></div>"}}],
[["test", 1], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=1 pron=I cond=c cond_code=Embed.Ov attested=Y ––><p style=\"text-align: center;\" hidden>Did you hear the new Taylor Swift album?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/1_3.png\" alt=\"Did you hear the new Taylor Swift album? Yeah! I’ll admit that I love listening to it while I’m at work!\"/></center></div>"}}],
[["test", 1], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=1 pron=I cond=d cond_code=Embed.Null attested=N ––><p style=\"text-align: center;\" hidden>Did you hear the new Taylor Swift album?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/1_4.png\" alt=\"Did you hear the new Taylor Swift album? Yeah! I’ll admit that love listening to it while I’m at work!\"/></center></div>"}}],
[["test", 1], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=1 pron=I cond=e cond_code=Prepos.Ov attested=Y ––><p style=\"text-align: center;\" hidden>Did you hear the new Taylor Swift album?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/1_5.png\" alt=\"Did you hear the new Taylor Swift album? Yeah! While I’m at work I love listening to it!\"/></center></div>"}}],
[["test", 1], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=1 pron=I cond=f cond_code=Prepos.Null attested=Y ––><p style=\"text-align: center;\" hidden>Did you hear the new Taylor Swift album?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/1_6.png\" alt=\"Did you hear the new Taylor Swift album? Yeah! While I’m at work love listening to it!\"/></center></div>"}}],
[["test", 1], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=1 pron=YouSg cond=g cond_code=Rt2.OV attested=Y ––><p style=\"text-align: center;\" hidden>Did you hear the new Taylor Swift album?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/1_7.png\" alt=\"Did you hear the new Taylor Swift album? Yeah, you already told me about it.  You love listening to it!\"/></center></div>"}}],
[["test", 1], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=1 pron=YouSg cond=h cond_code=Rt2.Null attested=N ––><p style=\"text-align: center;\" hidden>Did you hear the new Taylor Swift album?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/1_8.png\" alt=\"Did you hear the new Taylor Swift album? Yeah, you already told me about it. Love listening to it!\"/></center></div>"}}],
[["test", 2], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=2 pron=We cond=a cond_code=Rt.OV attested=Y ––><p style=\"text-align: center;\" hidden>How did your basketball game go?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/2_2.png\" alt=\"How did your basketball game go?  We lost the game unfortunately... \"/></center></div>"}}],
[["test", 2], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=2 pron=We cond=b cond_code=Rt.Null attested=Y ––><p style=\"text-align: center;\" hidden>How did your basketball game go?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/2_3.png\" alt=\"How did your basketball game go?  Lost the game unfortunately…\"/></center></div>"}}],
[["test", 2], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=2 pron=We cond=c cond_code=Embed.Ov attested=Y ––><p style=\"text-align: center;\" hidden>How did your basketball game go?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/2_4.png\" alt=\"How did your basketball game go?  I’m sad to report that we lost the game…\"/></center></div>"}}],
[["test", 2], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=2 pron=We cond=d cond_code=Embed.Null attested=N ––><p style=\"text-align: center;\" hidden>How did your basketball game go?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/2_5.png\" alt=\"How did your basketball game go?  I’m sad to report that lost the game…\"/></center></div>"}}],
[["test", 2], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=2 pron=We cond=e cond_code=Prepos.Ov attested=Y ––><p style=\"text-align: center;\" hidden>How did your basketball game go?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/2_6.png\" alt=\"How did your basketball game go?  Unfortunately, we lost the game…\"/></center></div>"}}],
[["test", 2], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=2 pron=We cond=f cond_code=Prepos.Null attested=Y ––><p style=\"text-align: center;\" hidden>How did your basketball game go?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/2_7.png\" alt=\"How did your basketball game go?  Unfortunately, lost the game…\"/></center></div>"}}],
[["test", 2], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=2 pron=YouPl cond=g cond_code=Rt2.OV attested=Y ––><p style=\"text-align: center;\" hidden>Did you hear our bad news?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/2_8.png\" alt=\"Did you hear our bad news?  You guys lost your basketball game… I’m sorry!\"/></center></div>"}}],
[["test", 2], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=2 pron=YouPl cond=h cond_code=Rt2.Null attested=N ––><p style=\"text-align: center;\" hidden>Did you hear our bad news?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/2_1.png\" alt=\"Did you hear our bad news?  Lost your basketball game… I’m sorry!\"/></center></div>"}}],
[["test", 3], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=3 pron=She cond=a cond_code=Rt.OV attested=Y ––><p style=\"text-align: center;\" hidden>New York City is my new favorite city, it’s so beautiful!</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/3_3.png\" alt=\"New York City is my new favorite city, it’s so beautiful! Nice! Carly has a request for you. She wants you to buy her an “I love NY” shirt next time.\"/></center></div>"}}],
[["test", 3], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=3 pron=She cond=b cond_code=Rt.Null attested=Y ––><p style=\"text-align: center;\" hidden>New York City is my new favorite city, it’s so beautiful!</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/3_4.png\" alt=\"New York City is my new favorite city, it’s so beautiful! Nice! Carly has a request for you. Wants you to buy her an “I love NY” shirt next time.\"/></center></div>"}}],
[["test", 3], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=3 pron=She cond=c cond_code=Embed.Ov attested=Y ––><p style=\"text-align: center;\" hidden>New York City is my new favorite city, it’s so beautiful!</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/3_5.png\" alt=\"New York City is my new favorite city, it’s so beautiful! Nice! Carly has a request for you. She told me that she wants you to buy her an “I love NY” shirt next time.\"/></center></div>"}}],
[["test", 3], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=3 pron=She cond=d cond_code=Embed.Null attested=N ––><p style=\"text-align: center;\" hidden>New York City is my new favorite city, it’s so beautiful!</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/3_6.png\" alt=\"New York City is my new favorite city, it’s so beautiful! Nice! Carly has a request for you. She told me that wants you to buy her an “I love NY” shirt next time.\"/></center></div>"}}],
[["test", 3], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=3 pron=She cond=e cond_code=Prepos.Ov attested=Y ––><p style=\"text-align: center;\" hidden>New York City is my new favorite city, it’s so beautiful!</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/3_7.png\" alt=\"New York City is my new favorite city, it’s so beautiful! Nice! Carly has a request for you. Next time, she wants you to buy her an “I love NY” shirt\"/></center></div>"}}],
[["test", 3], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=3 pron=She cond=f cond_code=Prepos.Null attested=Y ––><p style=\"text-align: center;\" hidden>New York City is my new favorite city, it’s so beautiful!</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/3_8.png\" alt=\"New York City is my new favorite city, it’s so beautiful! Nice! Carly has a request for you. Next time, wants you to buy her an “I love NY” shirt.\"/></center></div>"}}],
[["test", 3], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=3 pron=YouSg cond=g cond_code=Rt2.OV attested=Y ––><p style=\"text-align: center;\" hidden>Do you remember my request for your trip to New York City?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/3_1.png\" alt=\"Do you remember my request for your trip to New York City? Yes, you told me twice! You want me to buy you an “I love NY” shirt next time.\"/></center></div>"}}],
[["test", 3], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=3 pron=YouSg cond=h cond_code=Rt2.Null attested=N ––><p style=\"text-align: center;\" hidden>Do you remember my request for your trip to New York City?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/3_2.png\" alt=\"Do you remember my request for your trip to New York City? Yes, you told me twice! Want me to buy you an “I love NY” shirt next time.\"/></center></div>"}}],
[["test", 4], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=4 pron=They cond=a cond_code=Rt.OV attested=Y ––><p style=\"text-align: center;\" hidden>Ugh. I can’t get anything done when I’m at home. My parents cannot leave me alone.</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/4_4.png\" alt=\"Ugh. I can’t get anything done when I’m at home. My parents cannot leave me alone. It’s the same for me.  They wanted me to help them redecorate the living room yesterday!\"/></center></div>"}}],
[["test", 4], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=4 pron=They cond=b cond_code=Rt.Null attested=Y ––><p style=\"text-align: center;\" hidden>Ugh. I can’t get anything done when I’m at home. My parents cannot leave me alone.</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/4_5.png\" alt=\"Ugh. I can’t get anything done when I’m at home. My parents cannot leave me alone. It’s the same for me.  Wanted me to help them redecorate the living room yesterday!\"/></center></div>"}}],
[["test", 4], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=4 pron=They cond=c cond_code=Embed.Ov attested=Y ––><p style=\"text-align: center;\" hidden>Ugh. I can’t get anything done when I’m at home. My parents cannot leave me alone.</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/4_6.png\" alt=\"Ugh. I can’t get anything done when I’m at home. My parents cannot leave me alone. It’s the same for me.  I can’t believe that they wanted me to help them redecorate the living room yesterday!\"/></center></div>"}}],
[["test", 4], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=4 pron=They cond=d cond_code=Embed.Null attested=N ––><p style=\"text-align: center;\" hidden>Ugh. I can’t get anything done when I’m at home. My parents cannot leave me alone.</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/4_7.png\" alt=\"Ugh. I can’t get anything done when I’m at home. My parents cannot leave me alone. It’s the same for me.  I can’t believe that wanted me to help them redecorate the living room yesterday!\"/></center></div>"}}],
[["test", 4], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=4 pron=They cond=e cond_code=Prepos.Ov attested=Y ––><p style=\"text-align: center;\" hidden>Ugh. I can’t get anything done when I’m at home. My parents cannot leave me alone.</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/4_8.png\" alt=\"Ugh. I can’t get anything done when I’m at home. My parents cannot leave me alone. It’s the same for me.  Yesterday, they wanted me to help them redecorate the living room!\"/></center></div>"}}],
[["test", 4], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=4 pron=They cond=f cond_code=Prepos.Null attested=Y ––><p style=\"text-align: center;\" hidden>Ugh. I can’t get anything done when I’m at home. My parents cannot leave me alone.</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/4_1.png\" alt=\"Ugh. I can’t get anything done when I’m at home. My parents cannot leave me alone. It’s the same for me.  Yesterday, wanted me to help them redecorate the living room!\"/></center></div>"}}],
[["test", 4], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=4 pron=YouPl cond=g cond_code=Rt2.OV attested=Y ––><p style=\"text-align: center;\" hidden>Can you take the dog for a walk today?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/4_2.png\" alt=\"Can you take the dog for a walk today? Ugh. I can’t finish anything when I’m at home with you guys. You wanted me to wash the car yesterday!\"/></center></div>"}}],
[["test", 4], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=4 pron=YouPl cond=h cond_code=Rt2.Null attested=N ––><p style=\"text-align: center;\" hidden>Can you take the dog for a walk today?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/4_3.png\" alt=\"Can you take the dog for a walk today? Ugh. I can’t finish anything when I’m at home with you guys. Wanted me to wash the car yesterday!\"/></center></div>"}}],
[["test", 5], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=5 pron=I cond=a cond_code=Rt.OV attested=Y ––><p style=\"text-align: center;\" hidden>I woke up to the sound of my dog eating my couch this morning.</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/5_5.png\" alt=\"I woke up to the sound of my dog eating my couch this morning. That dog is destroying your life. \"/></center></div>"}}],
[["test", 5], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=5 pron=I cond=b cond_code=Rt.Null attested=Y ––><p style=\"text-align: center;\" hidden>I woke up to the sound of my dog eating my couch this morning.</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/5_6.png\" alt=\"I woke up to the sound of my dog eating my couch this morning. That dog is destroying your life. \"/></center></div>"}}],
[["test", 5], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=5 pron=I cond=c cond_code=Embed.Ov attested=Y ––><p style=\"text-align: center;\" hidden>I think that I woke up to the sound of my dog eating my couch this morning.</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/5_7.png\" alt=\"I think that I woke up to the sound of my dog eating my couch this morning. That dog is destroying your life. \"/></center></div>"}}],
[["test", 5], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=5 pron=I cond=d cond_code=Embed.Null attested=N ––><p style=\"text-align: center;\" hidden>I think that woke up to the sound of my dog eating my couch this morning.</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/5_8.png\" alt=\"I think that woke up to the sound of my dog eating my couch this morning. That dog is destroying your life. \"/></center></div>"}}],
[["test", 5], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=5 pron=I cond=e cond_code=Prepos.Ov attested=Y ––><p style=\"text-align: center;\" hidden>This morning I woke up to the sound of my dog eating my couch.</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/5_1.png\" alt=\"This morning I woke up to the sound of my dog eating my couch. That dog is destroying your life. \"/></center></div>"}}],
[["test", 5], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=5 pron=I cond=f cond_code=Prepos.Null attested=Y ––><p style=\"text-align: center;\" hidden>This morning woke up to the sound of my dog eating my couch.</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/5_2.png\" alt=\"This morning woke up to the sound of my dog eating my couch. That dog is destroying your life. \"/></center></div>"}}],
[["test", 5], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=5 pron=YouSg cond=g cond_code=Rt2.OV attested=Y ––><p style=\"text-align: center;\" hidden>So, you can’t go on vacation anymore and you have to pick up dog poop. You woke up to the sound of your dog eating your couch this morning. Are you sure you made the right choice?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/5_3.png\" alt=\"So, you can’t go on vacation anymore and you have to pick up dog poop. You woke up to the sound of your dog eating your couch this morning. Are you sure you made the right choice? This dog is destroying my life. \"/></center></div>"}}],
[["test", 5], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=5 pron=YouSg cond=h cond_code=Rt2.Null attested=N ––><p style=\"text-align: center;\" hidden>So, you can’t go on vacation anymore and you have to pick up dog poop. Woke up to the sound of your dog eating your couch this morning. Are you sure you made the right choice?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/5_4.png\" alt=\"So, you can’t go on vacation anymore and you have to pick up dog poop. Woke up to the sound of your dog eating your couch this morning. Are you sure you made the right choice? This dog is destroying my life. \"/></center></div>"}}],
[["test", 6], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=6 pron=We cond=a cond_code=Rt.OV attested=Y ––><p style=\"text-align: center;\" hidden>How was your Friday?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/6_6.png\" alt=\"How was your Friday? We had a nice dinner and then we saw a movie after work. I don’t remember what happened afterwards.\"/></center></div>"}}],
[["test", 6], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=6 pron=We cond=b cond_code=Rt.Null attested=Y ––><p style=\"text-align: center;\" hidden>How was your Friday?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/6_7.png\" alt=\"How was your Friday? Had a nice dinner and then we saw a movie after work. I don’t remember what happened afterwards.\"/></center></div>"}}],
[["test", 6], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=6 pron=We cond=c cond_code=Embed.Ov attested=Y ––><p style=\"text-align: center;\" hidden>How was your Friday?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/6_8.png\" alt=\"How was your Friday? I know that we had a nice dinner and then we saw a movie after work. I don’t remember what happened afterwards.\"/></center></div>"}}],
[["test", 6], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=6 pron=We cond=d cond_code=Embed.Null attested=N ––><p style=\"text-align: center;\" hidden>How was your Friday?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/6_1.png\" alt=\"How was your Friday? I know that had a nice dinner and then we saw a movie after work. I don’t remember what happened afterwards.\"/></center></div>"}}],
[["test", 6], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=6 pron=We cond=e cond_code=Prepos.Ov attested=Y ––><p style=\"text-align: center;\" hidden>How was your Friday?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/6_2.png\" alt=\"How was your Friday? After work, we had a nice dinner and then we saw a movie. I don’t remember what happened afterwards.\"/></center></div>"}}],
[["test", 6], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=6 pron=We cond=f cond_code=Prepos.Null attested=Y ––><p style=\"text-align: center;\" hidden>How was your Friday?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/6_3.png\" alt=\"How was your Friday?  After work, had a nice dinner and then we saw a movie. I don’t remember what happened afterwards.\"/></center></div>"}}],
[["test", 6], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=6 pron=YouPl cond=g cond_code=Rt2.OV attested=Y ––><p style=\"text-align: center;\" hidden>How was your Friday? You had a nice dinner. Did you guys see a movie?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/6_4.png\" alt=\"How was your Friday? You had a nice dinner. Did you guys see a movie? Yeah, after dinner we saw a movie.  I don’t remember what happened afterwards.\"/></center></div>"}}],
[["test", 6], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=6 pron=YouPl cond=h cond_code=Rt2.Null attested=N ––><p style=\"text-align: center;\" hidden>How was your Friday? Had a nice dinner. Did you guys see a movie?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/6_5.png\" alt=\"How was your Friday? Had a nice dinner. Did you guys see a movie? Yeah, after dinner we saw a movie. I don’t remember what happened afterwards.\"/></center></div>"}}],
[["test", 7], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=7 pron=He cond=a cond_code=Rt.OV attested=Y ––><p style=\"text-align: center;\" hidden>Can your dad drive us to the mall on Sunday?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/7_7.png\" alt=\"Can your dad drive us to the mall on Sunday? He can’t on Sunday. Maybe on Saturday, though. \"/></center></div>"}}],
[["test", 7], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=7 pron=He cond=b cond_code=Rt.Null attested=Y ––><p style=\"text-align: center;\" hidden>Can your dad drive us to the mall on Sunday?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/7_8.png\" alt=\"Can your dad drive us to the mall on Sunday? Can’t on Sunday. Maybe on Saturday, though. \"/></center></div>"}}],
[["test", 7], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=7 pron=He cond=c cond_code=Embed.Ov attested=Y ––><p style=\"text-align: center;\" hidden>Can your dad drive us to the mall on Sunday?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/7_1.png\" alt=\"Can your dad drive us to the mall on Sunday? He said that he can’t on Sunday. Maybe on Saturday, though. \"/></center></div>"}}],
[["test", 7], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=7 pron=He cond=d cond_code=Embed.Null attested=N ––><p style=\"text-align: center;\" hidden>Can your dad drive us to the mall on Sunday?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/7_2.png\" alt=\"Can your dad drive us to the mall on Sunday? He said that can’t on Sunday. Maybe on Saturday, though. \"/></center></div>"}}],
[["test", 7], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=7 pron=He cond=e cond_code=Prepos.Ov attested=Y ––><p style=\"text-align: center;\" hidden>Can your dad drive us to the mall on Sunday?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/7_3.png\" alt=\"Can your dad drive us to the mall on Sunday? On Sunday, he can’t. Maybe on Saturday, though. \"/></center></div>"}}],
[["test", 7], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=7 pron=He cond=f cond_code=Prepos.Null attested=Y ––><p style=\"text-align: center;\" hidden>Can your dad drive us to the mall on Sunday?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/7_4.png\" alt=\"Can your dad drive us to the mall on Sunday? On Sunday, can’t. Maybe on Saturday, though. \"/></center></div>"}}],
[["test", 7], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=7 pron=YouSg cond=g cond_code=Rt2.OV attested=Y ––><p style=\"text-align: center;\" hidden>Can I drive the kids to the mall on Sunday?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/7_5.png\" alt=\"Can I drive the kids to the mall on Sunday? You can’t because the car is still not working. Maybe on Sunday, though. \"/></center></div>"}}],
[["test", 7], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=7 pron=YouSg cond=h cond_code=Rt2.Null attested=N ––><p style=\"text-align: center;\" hidden>Can I drive the kids to the mall on Sunday?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/7_6.png\" alt=\"Can I drive the kids to the mall on Sunday? Can’t because the car is still not working. Maybe on Sunday, though. \"/></center></div>"}}],
[["test", 8], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=8 pron=They cond=a cond_code=Rt.OV attested=Y ––><p style=\"text-align: center;\" hidden>How are the kids doing?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/8_8.png\" alt=\"How are the kids doing? Great! We’re at the beach. They are building sandcastles, of course. I’ll send you a photo.\"/></center></div>"}}],
[["test", 8], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=8 pron=They cond=b cond_code=Rt.Null attested=Y ––><p style=\"text-align: center;\" hidden>How are the kids doing?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/8_1.png\" alt=\"How are the kids doing? Great! We’re at the beach. Are building sandcastles, of course. I’ll send you a photo.\"/></center></div>"}}],
[["test", 8], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=8 pron=They cond=c cond_code=Embed.Ov attested=Y ––><p style=\"text-align: center;\" hidden>How are the kids doing?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/8_2.png\" alt=\"How are the kids doing? Great! We’re at the beach, which means that they are building sandcastles of course. I’ll send you a photo.\"/></center></div>"}}],
[["test", 8], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=8 pron=They cond=d cond_code=Embed.Null attested=N ––><p style=\"text-align: center;\" hidden>How are the kids doing?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/8_3.png\" alt=\"How are the kids doing? Great! We’re at the beach, which means that are building sandcastles of course. I’ll send you a photo.\"/></center></div>"}}],
[["test", 8], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=8 pron=They cond=e cond_code=Prepos.Ov attested=Y ––><p style=\"text-align: center;\" hidden>How are the kids doing?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/8_4.png\" alt=\"How are the kids doing? Great! We’re at the beach. So, of course they are building sandcastles. I’ll send you a photo.\"/></center></div>"}}],
[["test", 8], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=8 pron=They cond=f cond_code=Prepos.Null attested=Y ––><p style=\"text-align: center;\" hidden>How are the kids doing?</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/8_5.png\" alt=\"How are the kids doing? Great! We’re at the beach. So, of course are building sandcastles. I’ll send you a photo.\"/></center></div>"}}],
[["test", 8], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=8 pron=YouPl cond=g cond_code=Rt2.OV attested=Y ––><p style=\"text-align: center;\" hidden>The kids are having a great time at the beach. Can you guess what we’re doing? I’ll send you a photo.</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/8_6.png\" alt=\"The kids are having a great time at the beach. Can you guess what we’re doing? I’ll send you a photo. You guys are building sandcastles, of course!  \"/></center></div>"}}],
[["test", 8], "AcceptabilityJudgment", {s: {html: "<div style=\"width: 50em;\"><!––  trial_type=test item_number=8 pron=YouPl cond=h cond_code=Rt2.Null attested=N ––><p style=\"text-align: center;\" hidden>The kids are having a great time at the beach. Can you guess what we’re doing? I’ll send you a photo.</p><center><img style=\"text-align:center;\" src=\"https://ryanchausse.com/aubrie_masters/images/conversation_pics/8_7.png\" alt=\"The kids are having a great time at the beach. Can you guess what we’re doing? I’ll send you a photo. Are building sandcastles, of course! \"/></center></div>"}}],
];