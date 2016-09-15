# coding=utf-8
import logging as log
import random

import secrets
import telegram
from time import sleep

sad_words = {"addolorato", "afflitto", "afflizione", "ambascia", "angustia", "autocommiserazione", "avvilimento",
             "cordoglio", "cupezza", "cupo", "demoralizzante", "demoralizzato", "depressione", "deprimente", "desolato",
             "desolazione", "disperato", "disperazione", "dispiaciuto", "dolore", "doloroso", "funereo", "infelice",
             "infelicità", "insoddisfatto", "insoddisfazione", "lugubre", "malessere", "malinconia", "malinconico",
             "mestizia", "mesto", "oppressione", "opprimente", "pena", "penoso", "sconfortato", "sconforto",
             "sofferenza", "solitudine", "straziante", "strazio", "tedio", "tedioso", "tetraggine", "tetro",
             "tristezza"}

random_poems = [
    "STRANEZZE DI UN INCENDIO.\nOgni cosa tra le fiamme si accende.\nTu invece ti sei spenta.",
    "SI PUO' MORIRE DI FEDE.\nEri in chiesa assorta\nin pensieri intensi\nma quella grossa croce\nti cadde proprio nei sensi.",
    "Dalla raccolta: \"Dipartita in partita\",\nSTRANEZZE DI UN VOLO.\nCadendo da quell'aereo tu salisti in cielo.",
    "Dalla raccolta: \"Urna e diurna\",\nULTIMO SALUTO.\nTi affacciasti da quel balcone\nper potermi salutare\nma solo il marciapiede\nti potè fermare.",
    "Dalla raccolta: \"Pietro, prima che canti il gallo, fai partire la base\",\nNOTE DOLENTI.\nMentre ascoltavi quella fuga di Bach\nnon ti accorgesti della fuga di gas.",
    "Dalla raccolta: \"Pietro, prima che canti il gallo, fai partire la base\",\nSAPORE DI MARE.\nFacesti il bagno dopo aver mangiato\nma a riva tornò solo\nquell'ottimo brasato.",
    "DISABITATO.\nQuando tu mi hai lasciato\nanche io me ne sono andato.",
    "LE TUE ULTIME PAROLE.\nDicesti: solo la morte ci dividerà.\nCi siamo divisi.",
    "Dalla raccolta: \"Io ho la luce tua, tu hai la leucemia\",\nHAI PRESO QUEL TRENO.\nHai preso quel treno\nlo hai preso in pieno.",
    "Dalla raccolta: \"Io ho la luce tua, tu hai la leucemia\",\nFACEVI SEMPRE CENTRO.\nTi gettasti dal balcone\nper via di quell'incendio\nma il telo dei pompieri\naveva un buco al centro.",
    "Dalla raccolta: \"C'è più spazio in casa da quando sei cenere\",\nTU AVEVI RAGIONE.\nIn quell'incidente\nche ti fu fatale\ntu avevi ragione.",
    "Dalla raccolta: \"C'è più spazio in casa da quando sei cenere\",\nLIBERTA'.\nVoglio una vita, dicevi, senza catene.\nE non le avevi nemmeno quando la tua auto precipitò\nin quella scarpata sulla neve.",
    "BREVE INCONTRO.\nTi conobbi al mare, ma poi affogasti.",
    "Dalla raccolta: \"La tua bellezza e' intatta anche dopo l'autopsia\",\nMI COPRISTI IL SOLE\nTi gettasti dal balcone, e mi copristi il sole.",
    "Dalla raccolta: \"La tua bellezza e' intatta anche dopo l'autopsia\",\nFRAMMENTI DI UN FRONTALE.\nHai sporcato il guard rail di rosso,\nil femore con la tibia sono piu' in la' nel fosso,\ne ancor piu' in la' giace nella scarpata\nla tua scatola cranica, non piu' ben confezionata",
    "Dalla raccolta: \"Io nell'universo e tu nell'obitorio\",\nGLI STRANI INCROCI DELLA VITA.\nTi fermasti prudente e a destra desti precedenza,\nma il tir entro' nella tua vita da sinistra",
    "Dalla raccolta: \"Io nell'universo e tu nell'obitorio\",\nTIRAMI SU.\nTu mi gridavi: 'Tirami su',\nma il mio braccio non ce la fece piu'.\nTi vidi andare in quel burrone giu'\nma poi non ci siamo visti piu'.",
    "Dalla raccolta: \"Coperta di mogano\",\nCORRENTE POETICA.\nRiparavi la lampada che illuminava la serra,\nma quel filo scoperto ti ha coperto di terra.",
    "Dalla raccolta: \"Coperta di mogano\",\nAH MARMI.\nAh marmi,\ngraniti colorati con le foto di ex malati che si sono addormentati\nsperando di essere svegliati.\nPietre scolpite coprite le vite,\nle vite diverse di queste anime perse,\nanche la vita di quell'amico poeta che scrisse sulla sua tomba: la vita e' una merda.",
    "Dalla raccolta: \"Coperta di mogano\",\nGIORNO DI RACCOLTA.\nQuel giorno non si apri' il tuo paracadute\ne sopra un campo roccioso esplodesti in salute.\nSparsa in frammenti come un puzzle enorme:\nsu un pezzo di prato riordinai le tue forme.",
    "Dalla raccolta: \"Mi illumino di incenso\",\nIL GIORNO DELLA RIESUMAZIONE.\nSei venuta fuori dalla cassa perfetta\ncome una banconota del Bancomat.",
    "LA GIOIA IMMENSA CHE SI TROVA NEL RIFLETTERE.\nChi prima chi dopo\ntutti quanti dobbiamo morire.",
    "Dalla raccolta: \"Mi illumino di incenso\",\nIL TUO RESPIRO.\nIl tuo respiro a volte leggero\nil tuo respiro a volte intenso\nieri era dolce\noggi è venuto meno.",
    "Dalla raccolta: Poesie religiose: \"Pietro, prima che canti il gallo, fai partire la base\",\nPER DISTRARTI UN PO'.\nSola in quel letto di ospedale\nmi sussurrasti \"è grave\".\nTi risposi \"no amore, durerà poco la tua croce\"\npoi per distrarti feci scegliere a te\nsu quel bel depliant...\nla tua cassa di noce.",
    "Dalla raccolta: \"Mettiamoci una pietra sopra\",\nTU NON POTEVI.\nTu non potevi parlare, eri muta\ntu non potevi ascoltare, eri sorda\ntu non potevi guardare, eri cieca\ntu non potevi abbracciare, eri morta.",
    "Dalla raccolta: \"Mettiamoci una pietra sopra\",\nSENZA UNA RISPOSTA.\n«Cosa ci faccio a questo mondo,» - mi chiedo\n«quando scopro che intorno a me c'è gente che muore,\nE tu! Ragazzina! Te lo chiedi? Ragazzina!\nTu te lo chiedi? Ragazzina! Ragazzina! RAGAZZINA!!\nCosa ci faccio a questo mondo,\nquando scopro che intorno a me c'è gente che muore,\nSOLO INTORNO A ME.»",
    "Dalla raccolta: \"Do re mi fu\",\nPATITA DEL ROCK, sottotitolo: CHITARRA ELETTRICA.\nSuonavi bene la tua chitarra\nQuell'ultima nota\ncon la scala di corrente\ndel tuo assolo\nfu l'unica nota dolente.",
    "Dalla raccolta: \"Fiato alle trombosi\",\nNOTTE DI S.LORENZO.\nTu guardavi le stelle cadenti e facevi festa.\nPoi, una ti colpì... proprio sulla testa.",
    "Dalla raccolta: \"Coma tu mi vuoi\",\nPOESIA PER UN AMICO.\nVolevi far festa\ncon la tua nuova Ford Fiesta\nma la sua scocca troppo leggera\na quell'autosnodato che ti veniva d'avanti non tenne testa.",
    "Dalla raccolta: \"Sei morta ovvero il giorno della trasfusione non eri in vena\",\nLA CRISI DEL 7 ANNO.\nNon ho i soldi per pagare la tua riesumazione.",
    "Dalla raccolta: \"Io ho la luce tua, tu hai la leucemia\",\nMORTE IN DIRETTA.\nTi impiccasti sulla terrazza\nall'antenna del nostro televisore,\ncosì davanti a quello schermo vidi saltare,\ntutti i programmi del nostro amore.",
    "Dalla raccolta: \"Urna e diurna\",\nCOINCIDENZE FERROVIARIE (TI RIMBORSARONO IL BIGLIETTO).\nQuella bomba viaggiava proprio sul tuo treno\nproprio sul tuo vagone\nproprio nel tuo scompartimento\nproprio sotto il tuo posto."
]


def handle_update(update):
    if update.message:
        text = update.message.text
        chat_id = update.message.chat.id
    elif update.edited_message:
        text = update.edited_message.text
        chat_id = update.edited_message.chat.id
    else:
        log.info("Unable to find text in update. Going to skip it.")
        return

    mp_bot = telegram.Bot(token=secrets.mino_pausa_bot_token)

    if text == '/start':
        mp_bot.sendMessage(str(chat_id), "Mino Pausa bot is running.", disable_web_page_preview=True)
    elif sad_message(text):
        log.info("Sad keyword found.")
        sleep(3)
        mp_bot.sendMessage(str(chat_id), "Per piacere...", disable_web_page_preview=True)
        sleep(5)
        mp_bot.sendMessage(str(chat_id), "Per piacere...", disable_web_page_preview=True)
        sleep(7)
        mp_bot.sendMessage(str(chat_id), random.choice(random_poems), disable_web_page_preview=True)
        log.info("Random poem sent.")


def sad_message(text):
    return len(set(text.lower().split(" ")) & sad_words) > 0


def get_status():
    return "Mino Pausa Bot is running."
