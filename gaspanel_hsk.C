#include "attrib.C"
#include <cstdio>
Int_t* GetColors( Int_t type, Int_t ndata );

void gaspanel_hsk( const char* fname = "/home/kmcbride/hsk_plotter/helix_hsk_plotter/hsk_store_2024-01-29_02:36:48.587921000Z.root" )
{

  // timestamp epoch start is 
  // 1696991228.568563
  // and interesting stuff happens on 10/12/2023 at Central time 9AM
  // which is 1697119200
  // and the start of overnight pumpdown is: 1697137620.0
  TFile *f = new TFile( fname );
  if( !f->IsOpen() ) return;
  TTree *fTree = (TTree*)f->Get( "t" );
  if( !fTree ) return;
  TGraph * gCO2 = new TGraph();
  TGraph * gAr = new TGraph();
  TGraph * gMixed = new TGraph();
  HLX_HSK_MainHSKState fMainState; // apparently this doesn't have the timestamp in it, so we need to use also another class that does...
  HLX_HSK_PowerState fPowerState;
  TBranch *b_hsk_fMainState;
  TBranch *b_hsk_fPowerState;
  fTree->SetMakeClass( 1 );
  fTree->SetBranchAddress("fMain", &fMainState, &b_hsk_fMainState);
  fTree->SetBranchAddress("fPowerState", &fPowerState, &b_hsk_fPowerState);
  Int_t nevt = fTree->GetEntries();
  Double_t toffset = -1;
  Double_t tlast=0;
  // get and fill the main hsk power variable
  for( Int_t i = 0; i < nevt; i++ ) {
    fTree->GetEntry( i );
    //TTimeStamp ts   = fRICHState.fTimeStamp;
    TTimeStamp ts   = fPowerState.fTimeStamp;
    // time stuff so leave it alone
    Double_t   time = ts.GetSec()+ts.GetNanoSec()*1e-9;
    if( i == 0 ){
      toffset = time;
      printf("%f", toffset);
    }
    tlast=time-toffset;
    // access your var
    Float_t mainhskpower = fPowerState.fMainHSKPower;
    //Float_t mainhskpower = 28;
    //fDCTFlowsCO2_p =
    HLX_HSK_MainFlows fDCTFlowsCO2 = fMainState.fFlowMeterCO2;
    HLX_HSK_MainFlows fDCTFlowsArgon = fMainState.fFlowMeterArgon;
    HLX_HSK_MainFlows fDCTFlowsMixed = fMainState.fFlowMeterMixed;

    // put the data into the TGraph
    gCO2->AddPoint(time-toffset,fDCTFlowsCO2.mass);
    gAr->AddPoint(time-toffset,fDCTFlowsArgon.mass);
    gMixed->AddPoint(time-toffset,fDCTFlowsMixed.mass);
    //g->AddPoint(time-toffset,mainhskpower);
    //printf("%d", i);
  }
  // check attrib
  Attrib( 20, 24, 24, 1.2, 1.7 );
  Int_t *col = GetColors( kBird, 3 );
  TCanvas *c1 = new TCanvas( "c1", "", 800, 800 );
  // check frame, this has to be the correct x and y values for the axes
  Double_t maxy=1.1*TMath::MaxElement(gCO2->GetN(),gCO2->GetY());
  Double_t miny=0.9*TMath::MinElement(gCO2->GetN(),gCO2->GetY());
  Double_t maxx=1.1*TMath::MaxElement(gCO2->GetN(),gCO2->GetX());
  Double_t minx=0.9*TMath::MinElement(gCO2->GetN(),gCO2->GetX());
  //TH1F *frame = gPad->DrawFrame(1697119200.0-toffset, miny, 1697137620.0-toffset, maxy );
  //TH1F *frame = gPad->DrawFrame(0, miny, 7200, maxy );
  TH1F *frame = gPad->DrawFrame(0, 0, 7200, 250 );
  frame->GetXaxis()->SetTitle( "Time (sec)" );
  frame->GetYaxis()->SetTitle( "Flow" );
  TLegend *leg = new TLegend( 0.65, 0.90, 0.87, 0.98);
  AttribL( leg, 0.15, 20, 23 );

  gCO2->Draw();
  AttribG( gCO2, 1, 5, 1,3);
  AttribG( gAr, 2,   3, 2,3);
  AttribG( gMixed, 4, 4, 3,3);
/*void AttribG( TGraph *g, Int_t col, Int_t msty, Int_t lsty )
{
  g->SetMarkerStyle( msty );
  g->SetMarkerColor( col );
  g->SetLineStyle( lsty );
  g->SetLineColor( col );
}*/

  gAr->Draw("Same L");
  gMixed->Draw("Same L");
  leg->AddEntry( gCO2, Form("CO2"), "L" );
  leg->AddEntry( gAr, Form("Argon"), "L" );
  leg->AddEntry( gMixed, Form("Mixed"), "L" );
  leg->Draw();
  c1->SaveAs( "gaspanel.pdf" );
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

