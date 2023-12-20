#include "attrib.C"
#include <cstdio>
Int_t* GetColors( Int_t type, Int_t ndata );

int test_chain(const char *dirname="/home/keith/hsk_files", const char *ext=".root"){
  //TFile *f = new TFile( fname );
  //if( !f->IsOpen() ) return;
//fSoftwareUptime
  TChain mychain("t");
  TSystemDirectory dir(dirname, dirname);
  TList *files = dir.GetListOfFiles();
  if (files) {
    TSystemFile * file;
    TString fname;
    TIter next(files);
    while ((file=(TSystemFile*)next())) {
      fname = file->GetName();
      if (!file->IsDirectory() && fname.EndsWith(ext)) {
        printf("%s",fname.Data());
        mychain.Add(fname.Data());
      }
    }
  }

  //mychain.GetListOfFiles()->Print();
  //mychain->SetBranchAddress("dth",&dth);
  //HLX_HSK_PacketStats * packetstats = new HLX_HSK_PacketStats;
  Float_t softup;
  TH1D * h1= new TH1D("h1","h1", 1000, 0.0, 10000.0);
  printf("\n N branches %d",mychain.GetNbranches());
  printf("\n N trees %d",mychain.GetNtrees());
  //TObjArray *branches = mychain.GetListOfBranches();
  //TObjArray *leaves = chain.GetListOfLeaves();

  mychain.SetBranchAddress("fSoftwareUptime", &softup);
  //mychain.SetBranchAddress("fPacketStats", packetstats);

  Int_t nevt = mychain.GetEntries();
  printf("\n %d",nevt);
  printf("\n");

  for( Int_t i = 0; i < 1; i++ ) {
    mychain.GetEntry(i);
    // put the data into the TGraph
    h1->Fill(softup);
    printf("%f", softup);
  }
  // check attrib
  //Attrib( 20, 24, 24, 1.2, 1.7 );
  //Int_t *col = GetColors( kBird, 8 );
  TCanvas *c1 = new TCanvas( "c1", "", 800, 800 );
  // check frame, this has to be the correct x and y values for the axes
  //Double_t maxy=1.1*TMath::MaxElement(g->GetN(),g->GetY());
  //Double_t miny=0.9*TMath::MinElement(g->GetN(),g->GetY());
  //TH1F *frame = gPad->DrawFrame(0, miny, tlast, maxy );
  //TH1F *frame = gPad->DrawFrame(0, 0, 7200, 50 );
  h1->Draw();
  c1->SaveAs( "test_chain.pdf" );
  return 0;
}


Int_t* GetColors( Int_t type, Int_t ndata )
{
  gStyle->SetPalette( type );
  Int_t ncol = TColor::GetNumberOfColors();
  Int_t FI = TColor::GetColorPalette( 0 );
  Int_t *col = new Int_t[ndata];
  for( Int_t i = 0; i < ndata; i++ ) 
    col[i] = FI+ncol/ndata*i; 

  return col;
}

