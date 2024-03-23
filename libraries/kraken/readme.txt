kraken is a turn-key OCR system optimized for historical and non-Latin script material.

links {

  https://digitalorientalist.com/2019/11/05/using-kraken-to-train-your-own-ocr-models/

}

Kraken is not equipped to handle every text {

  I recommend using it only on works for which you have clear PDFs or page
  images (300 DPI is the usual recommendation) and in which the text is laid
  out in one column.

  If you are starting from a PDF, use your tool of choice to separate the pages
  into individual image files. I use pdftoppm or ImageMagick’s convert tool,
  and I have been able to use Kraken with PNG, TIFF, and JPG files.

}

Kraken ist eine weiterentikicklung der OCR-Software OCRopus, die für Hand- und Druckschriften geeignet ist.

Kraken is related to eScriptorium {
  einer Plattform zur manuellen oder automatisierten Segmentierung und
  Texterkennung von historischen Handschriften und Drucken. 

  eScriptorium provides a user-friendly interface for annotating data, training
  models, and inference (but also much more).
}

Training own models {

  While I did not have any luck with Kraken’s pretrained models, I was
  successful with quickly training my own models, a process which I jumpstarted
  using Kraken’s ability to produce artificial training data from a selected
  font and text.

  ketos {
    https://digitalorientalist.com/2023/09/26/train-your-own-ocr-htr-models-with-kraken-part-1/

    transcribe {

      If you would like to transcribe training data yourself, Kraken offers a
      built-in transcription environment that is hosted locally in your
      browser. See the instructions and options for the ketos transcribe
      command -> http://kraken.re/ketos.html#transcription

    }

  }

  Preparing AI training data {

    In this guide, however, we are automatically generating training data, and
    for this we need
      1) a font that is close to the typeface of what we want OCRed, and
      2) a sample text which contains all of the characters we want the
         computer to be able to identify.

  }

}

OCR general notes {
 
   - high quality scans
       - 300 dpi+ 
       - lossless format (tiff, png) -> extract images from pdf with pdftocairo or pdfimages
           https://stackoverflow.com/a/30274288/180275 says
              « If you convert to JPEG, you will always have the type of artifacts you are seeing. »

   - Only features that are found in the training data can later be recognized,

   zenodo: OCR/HTR (Handwritten text recognition) model repository {

     https://zenodo.org/communities/ocr_models/records?q=&l=list&p=1&s=10&sort=newest


   }

}

Fred's textcleaner script {

   http://www.fmwconcepts.com/imagemagick/textcleaner/index.php

   This script processes a scanned document of text to clean the text
   background 

}

Scantailor https://github.com/scantailor/scantailor 
   A fairly user-friendly software for semi-automatic batch processing of image scans
