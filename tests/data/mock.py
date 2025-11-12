# -*- coding: utf-8 -*-
# Copyright (C) 2021 GIS OPS UG
#
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.
#
import datetime
import random

PARAM_POINT = [8.34234, 48.23424]
PARAM_LINE = [[8.688641, 49.420577], [8.680916, 49.415776]]
PARAM_LINE_MULTI = [[8.688641, 49.420577], [8.680916, 49.415776], [8.780916, 49.445776]]
PARAM_LINE_OPTIMIZED = [
    [8.688641, 49.420577],
    [8.680916, 49.415776],
    [8.720916, 49.435776],
    [8.780916, 49.445776],
]
PARAM_POLY = [[[8.688641, 49.420577], [8.680916, 49.415776]]]

PARAM_INT_BIG = 500
PARAM_INT_SMALL = 50

PARAM_STRING = random.choice("abcdefghijklmnopqrstuvwxyz")

PARAM_GEOJSON_POINT = {"type": "Point", "coordinates": PARAM_POINT}
PARAM_GEOJSON_LINE = {"type": "LineString", "coordinates": PARAM_LINE}
PARAM_GEOJSON_POLY = {"type": "Polygon", "coordinates": PARAM_POLY}

ENDPOINTS_RESPONSES = {
    "valhalla": {
        "directions": {
            "trip": {
                "legs": [
                    {
                        "shape": "}wpulAvkxblCtJpGu}@hrCkAvDsAdEm@xBkAvDeK`\\ssAthE{iAjpDyiAlpD",
                        "summary": {"length": 100.32, "time": 25},
                    },
                    {
                        "shape": "}wpulAvkxblCtJpGu}@hrCkAvDsAdEm@xBkAvDeK`\\ssAthE{iAjpD",
                        "summary": {"length": 50.12, "time": 32},
                    },
                ]
            },
            "units": "kilometers",
        },
        "alternatives": {
            "trip": {
                "locations": [
                    {"type": "break", "lat": 42.358528, "lon": -83.2714, "original_index": 0},
                    {"type": "break", "lat": 42.43892, "lon": -82.749855, "original_index": 1},
                ],
                "legs": [
                    {
                        "summary": {
                            "has_time_restrictions": False,
                            "has_toll": False,
                            "has_highway": False,
                            "has_ferry": False,
                            "min_lat": 42.350438,
                            "min_lon": -83.275885,
                            "max_lat": 42.456438,
                            "max_lon": -82.869245,
                            "time": 2308.26,
                            "length": 46.176,
                            "cost": 3735.242,
                        },
                        "shape": "_ojxoAjmny}CpzAuA~EETt_@Tjj@P|]H~OHpRDvGNxLBnBFrDJ|J}EfA_@VsK`EaH~BiFpBqKbE}B~@q@TiC|@iHvB_FpAgGnAqKhBqQpAsIP_KPgQZq_@b@ic@\\sGHwBBiMFuf@~@ic@`@}GJ}TVmMNmOPkCBkSTa]^iDDeEFeGHgFJ_ED}HL_IJmABgCDeA@mLNuCG}`@VgLX}Qb@mIRk_@v@_[p@ka@ZqIDgLH_DD}W`@_A@oJPwEDoKJcVVog@f@aK@sE?aXBqC@}HKoEIe_@m@aCCeMG{F?{S_@wx@yAga@s@cLS_AA}FGwCCurAoAsEA}@Eqb@?_V]oK?egAdB{ENmw@Nif@vBmDHg^~AmPr@yDNcCRgDZeL~@on@nAyWtAsa@zEsIbAiFl@cHj@eDJySn@oFP{\\fAuMR_FHG{FI_IQcQGyFE{IyB}]i@sH}GwlAwD}q@kE{w@gDkaA}Hu{@}@qh@Q_f@?enA@oo@@qbA^uaBb@{eBxAigAt@ge@hAihCz@kr@dAilETg_AKspAGeoA]wv@eBcyDDgNDyI^iStD}q@nCwWpDkWzBkMxB{K|FsV|G}UzDmLbEcL`JgTfHyN`FeJ|HiMlIsLjv@saA|tAy_Bj]}c@hj@a{@jLyQ|GwKvNsWvMuVvWii@`IoQhHuQrQ{h@jFgS~CaOrEkVzCcTpCoVrCoW~@gQl@eQpAak@p@g`@d@g`@\\kk@Dub@Ge`@We`@q@ek@w@ca@gAcb@cDq~@gBs_@_Cub@eJcvAyBw_@sFa}@aDobAs@a_@e@}_AMqp@AmXU_b@[gvDm@_zAgB_vAyAks@mAyo@e@gQgB_y@e@qXo@kRy@wi@_Ake@]kW_@ux@Gw}@Iqe@S{k@K{uEYorAQg~AOk}AYm[mA{ZaB}W_BeRwBoReEuWyEwToEmRkEgOcJg[{AgGioAqdFmOeq@eMsm@eJwh@iIsf@cs@cgF_Kkt@a~@y_HuB_Pqb@{bDuGuh@yC_\\gAmLqC}_@gC{_@iDov@_A_WeAcc@s@}w@Fay@`@wnBX_cA?_ZDu{ELwt@CiYDa`@x@_f@z@qXpAiYhAaRtBqYtBsSvBoR|B{QpCkRhA{GzB{LvF}YfEoQnGkXrOqi@rJcY|\\yw@|G{LbCyFjKqRdR_XzQyUdJcKbLaKlZkTxPaKlHoDpOyHfKcE|UsGn\\gHhSaCfTo@vES|JM|JBvO`@dRLth@Bp_BxDdo@\\j\\{@jq@uDzSyCzMeC`TcElQaFbTaHvZwLzMgGvZcPlOgJjRiM|KsI|UcSh]e`@xWg^|JwQ|I_QpOm]|Ke\\jQao@te@ugB~V{_A|Jg_@bs@kjCzWqaAnS_w@v_@}vAbMae@hg@}jBnM_f@``@kwAzb@a_B~AsGzF}TnTku@jm@crBdl@{iBl\\ojAxf@oaBpm@{pBxGcUzc@cmAhe@snAhToj@|t@_mBtSoi@|EcMbSgi@bPof@lL_c@vWckAzNmt@rKkj@pJ{UbJu`@xJc^fMy_@vLiXhMcWvKoSnL}QfIaLhGgHpGcG`BaBbGgH`HkGjQmPfFkF~BwDlD{FrDqIlD_LlCiOhAaLrCs_@dDkd@lJ_sAF{DBqBIwHmBaUoAcG{HuXqHyWaEyN{^awAwHyWsHqRigAu_FotAurGmZuqAmXqpA{Mih@u^ihAs\\{w@yWyh@_CyEcMgUsgA_tByIoPspA{`Cqk@}`Aa^ol@wEeH}Usa@_t@eoAse@u|@{h@ukAcAkC_KsWuYuu@kXmr@aFmMaCgGwa@yjAgPmg@_BqE_c@iyA}IkZuPin@wWa~@eRim@mUeo@kYyo@sH_Po^qp@eKaQiVqc@qNmVoDoGgTw_@mLwSao@qjAwB}DoFoJuO_[gQu^eQaa@_GyOel@wjBgYcfAqNsk@wMki@maB{mGaO}i@e\\wnAkb@y|AySi{@og@moB}CuLi]mrAeHyUiS}i@mQq`@s\\mk@sVo\\i]g]}]aXmMwJqFsDoIeFgUgNcPuIwZgUqSiQkJoJ}IeKeXo`@eFsI}E}IkL{VqEaLiFyNsDoLsG_VuFcW_EiUgBiLaVkqBwSykByIqu@cJkp@wHwe@}Hea@eP_r@gNyf@u]{mAwPin@aNme@{S_r@q~@gzCeVmy@sr@o`Co@}BmX{bAkH{WwNqm@}Oiv@mCiP{Jwm@kBmLm[ahDqB{\\yAks@iA}dANk`@\\ixACwf@e@kh@oA}e@yC{h@}Fag@mEw]_EiWsGy]}DuQwJo`@sK{^{Xgz@s]_o@}P_YaT{[cIeLiS{Z_I}KokAycB}OwUaKkPaJkPyMeXoGoN}V}x@cOq`@oHuYyh@alCmYkxAw~@sxEg[uiBso@}kEeLqz@iDeUoGq^kGya@iOo}@eEqW{EmZcV}zAwHed@iRcdA{^igBiRc~@{hAinFsWwpAeTgeAcHu_@kHmd@cFaZ_WwfBoLep@yIs^iUuu@cDkJgg@ygAcUm_@mHqKsH}KydA{{AcgAw~Awd@aq@mEqGy_AusAaCmD{`@al@yp@qbAmpA{kBMUsPiWgSw]q]wp@eJoR{ByFcHgPoGkOw`@qbAaMuYyT{e@{IqO_Vma@yL_RuNqSmVs[gL}M{BiCcUcUwToSq[gX{u@yi@cf@{\\ifBcpAej@s`@gJkHeYmSyp@gg@y[qTs[oTccAim@gjBqdAigAii@yb@eUaQ_J}dAwi@k`@_Q}f@gRmdC_z@wf@qPysEa}Ag]kLmw@_WwTaHaTmJmbAgb@{QiJgUwM{GuBmDiAyMiEwKmD{Bo@aEiAiDaA|@iGf@{DrAyJNkA`@yCdAeI`DoVlZmrBzD{W~c@yzCj@sDb@wCbJgn@dJqm@rFg_@x@gFfS{yA~@{GlB{M|@wFlDuUvIum@nBqQpAwQn@eKq@iGnK_s@nRapAhBwLj`@uiCvPqhAjP{eAzPoiAbN_`AdPcgAnIak@`Jim@|Kut@t@qFxEk[pGyb@tAgJbJim@nHmf@bDeTzGqd@`G}^n@eEvDsVzEk[|CkSrAwInI_j@zJso@rQaiAfCiPr@kErDuUbDoSrl@q_EdKwq@bQmoAdBaN`Q{lA^eGXcIwF}@yDo@{BWs^cEgAMaI}@iX_CcW_@ca@`@iFF{CBaj@AgB?sICqNQoJKqMOqBCoRWuBCeKM{T[iDE_DFuHP}UbAaDLqWfA}UbAiWbAwETcFRoDDmFFsAEeBK{IkA_KiCi@OsQwDiTiGsScGqDaA{N}DqQ{E}PuEoh@mNqIaC}b@}Lq^{Jo^{JmTaGyTgG_Y_I{MwDqLeDaFqAiZ{Hy@Suj@mNeHaBiKaCyS}EqCq@mU_GcLqA_T}@gLtB{An@iFrBkHfF{HtHgFvGqGfMyDxLqBpK_QxdAyClQnFbDtAkJ~BmOlDiPdJih@_G}EuRsGiBWwUmDqLa@k^bAeNw@qPkBwLuGiJ_NmD{Ky@wNdCuPrPcX~^_l@vNgd@rLo\\rImNdVgP`LuHzMyH",
                    }
                ],
                "summary": {
                    "has_time_restrictions": False,
                    "has_toll": False,
                    "has_highway": True,
                    "has_ferry": False,
                    "min_lat": 42.350438,
                    "min_lon": -83.275885,
                    "max_lat": 42.456438,
                    "max_lon": -82.869245,
                    "time": 2308.26,
                    "length": 46.176,
                    "cost": 3735.242,
                },
                "status_message": "Found route between points",
                "status": 0,
                "units": "kilometers",
                "language": "en-US",
            },
            "alternates": [
                {
                    "trip": {
                        "locations": [
                            {"type": "break", "lat": 42.358528, "lon": -83.2714, "original_index": 0},
                            {"type": "break", "lat": 42.43892, "lon": -82.749855, "original_index": 1},
                        ],
                        "legs": [
                            {
                                "summary": {
                                    "has_time_restrictions": False,
                                    "has_toll": False,
                                    "has_highway": False,
                                    "has_ferry": False,
                                    "min_lat": 42.356887,
                                    "min_lon": -83.275885,
                                    "max_lat": 42.496507,
                                    "max_lon": -82.869245,
                                    "time": 2837.547,
                                    "length": 54.324,
                                    "cost": 4493.543,
                                },
                                "shape": "_ojxoAjmny}CpzAuA~EETt_@Tjj@P|]H~OHpRDvGNxLBnBFrDJ|J}EfA_@VsK`EaH~BiFpBqKbE}B~@q@TiC|@iHvB_FpAgGnAqKhBqQpAsIP_KPgQZq_@b@ic@\\sGHwBBiMFuf@~@ic@`@}GJ}TVmMNmOPkCBkSTa]^iDDeEFeGHgFJ_ED}HL_IJmABgCDeA@mLNuCG}`@VgLX}Qb@mIRk_@v@_[p@ka@ZqIDgLH_DD}W`@_A@oJPwEDoKJcVVog@f@aK@sE?aXBqC@}HKoEIe_@m@aCCeMG{F?{S_@wx@yAga@s@cLS_AA}FGwCCurAoAsEA}@Eqb@?_V]oK?egAdB{ENmw@Nif@vBmDHg^~AmPr@yDNcCRgDZeL~@on@nAyWtAsa@zEsIbAiFl@cHj@eDJySn@oFP{\\fAuMR_FHG{FI_IQcQGyFE{IyB}]i@sH}GwlAwD}q@kE{w@gDkaA}Hu{@}@qh@Q_f@?enA@oo@@qbA^uaBb@{eBxAigAt@ge@hAihCz@kr@vDemBjAafA^ay@d@oTDgC`@_XHkKN{OLi\\Cg~AUqh@y@acBm@swABuOPaQp@ob@JqGhAmPrCcVjEg[xGw\\xK_b@fYgt@tF_MrPqYpLwObt@c{@llAitAjUgYjV}[hK}NlSu]dRc\\nn@akA`DoGzIeQ`HwMzZk_A`Lcf@~Lox@vCu`@`B{]pCw_AhBswAl@aiA_@it@yEuvByFcjAyFs~@wCgj@iDsq@m@aMqCsu@eDqzAQkQm@gj@Xct@l@coBt@qhAf@ot@l@u{BOoPWaOg@uOgBg[wCgf@?yOcJqxA_Bm_@{Ck}@wAyk@WuMe@ij@_@_l@MuoAPgmCc@s}AEmPe@gpEk@ojAe@q]mCmg@cEac@}E{YqGa^eJe_@aKc_@gIc\\_B_HoA}FyBiI{g@usB{Uk_AoSmz@mJob@mX{zA{WuzBoOokAiaBazLkS{zAeFye@_A_KYkD_BsSuBiW{AkTgBmXgD_r@kAo^s@cXQsZ]qZEck@\\}iCRgfDfA{cCzDceAOkOn@cKbEyw@bHkoAlC_n@r@__@RgXa@aTIoEG_JsAa`AqCmfBaA_k@y@ye@iBuR_DgOmEcNgG}KmXwZiQeSmFyG}BeCqAkBeB}CoAaDiAwDo@eDe@kEMuBOcDKeSCeFAyBk@a~@_@sQMmF{@y\\OmGk@wWOqG[}NQeIy@i`@{@ka@WeMMkGWmJUyI[sU]wRB_LDaF?oFGeAEw@YsCQmAYaB]uAiAcEuMuZ{@wCcAkD{Lqc@wIo[uEsPsTcx@sEkPwGcV}@aDcAoDuCaKeCeJwEcQcQ_n@uLqb@{A}FiA_F}[ikAsCqK_DcLa@yAaBcGkAgE_BcGuBuHmBeHwAgFyCqK[kAg@oB_IsZcUc{@}Is\\oEoP]uAyEkQ}BuIyAqF{@eD_AiDoGuUgBuGwBeIaUyy@oLcc@mAoE_B_HeCwJiK_`@uH{XuAaFuDeNkAwEmAqEkEiR_@wAwDyN_BgGiBgHQm@uBqHqBkHgBsGwAqF{@}CaBcGcHaWw[_lAkEiPgD_MmCcKeA{DuAkFaAmDyAkFaD_M{BaI{HqYkMue@uMkf@uAcFuE_QeDuLmAmEcAqDoDyMQo@kDsM_Scu@mM}e@gCiJyAqFmCaKiC_JkA}DPkGaAkDiDyI_EiK{Ms\\Wo@eDeI_D{GsCaG}BwDgDsF{DmFiMyP{B}CcMwOaO}S{FyJ}F{LeCuFeC{HiC{JsBsJiBoKyKcr@uEoXaEcRsDkOkP_j@wM_j@cq@}rCkTy~@s_@{{AoJaa@_R{r@uU_|@{kBycH_m@_xBoVw}@wK}`@{VsfAgQav@}Nkt@iEsTqEySsSyt@gB_IiBaK{AgK_LcdAyAsKwF{d@iB{LoLez@{Hmf@Ik@eCmRuA{Kc@_C{@{E}AgGeC}IuCaJoDeHoCoEkEaGaDqDaD}CwDyCaF_DiH}DwKuCaIm@_E[kHJkEX_Gp@wHhBeI~CmFdDuCpBmJxGoHjImQ~QcJjHyYhYeK|KaWnUsMnUmr@~n@sj@lj@s\\v\\cPhOoJfK{j@vj@wvAvkAiiAn{@ke@h^cXlS_\\xVc~BllB_h@vb@sf@h_@ygC`fBwStMkN|HqRdJqJpD{NjEgNzCmN|BkKhAoLz@mOp@q^r@{Yr@qw@rAuoBfMib@xCyPt@ex@tEclFnGar@l@_~ArAk~@jCasC~@e\\g@kVeAmPgA{l@gFgUmBkX}@sQg@qQUue@HsNNoW`@oI\\uAF{G\\up@p@mu@|AqWh@ytAdD{g@pAiLPaq@n@{eAn@mXxAo_@fEwK`C_GzA{YvJ}RrIyOhJcSjMq\\v[}NvPwLfOsFnJgFzJyJbRmOlYaO~\\yJrYqMnj@sC|OmGn]}Glb@yLdy@kLts@_DhNgHtX}KzXmMdYoKrQoOrTyOxSwTtQoOdJiNzHmj@dQgu@hUqQpEe_AxVob@jMyXlJ_uAre@_`A|\\ixBrr@aw@bTekA|XeSd@qc@fH{d@vEwI|@eOvAkIv@aM\\i]y@uJ}BqSuByOuDePaIgMmIgMcNuG{KcIcRc@{AoJ_Z}Da[{Kcy@cAyF}@_TwBep@e@oQSeJOoJQwLQiQkCmd@Gix@?}ZMybAOkvAAuKGed@e@mfDc@i`CQygAM}Pc@aPq@{P}AyVyBqUqC}UiDgT{C{OkDsOeDeNiDkLoDaL}EiNcFcMcGqMaFmKsHiNgKmP}KqOoSgVaMyLuHiGoHcGaf@m[_d@}YshAeu@cbAgo@mVwOeWiPceAgr@eqBgrA}w@ch@iSwMqLiIcJwHoJcIyG_HuF{FoKoMmIcLwEaHqEkHeH_MgG}L{FoMsEiLgEwKgE}NcFaRgEuQyCgOqBoL{A}J}AgLoAgLwAqPcAiN{@uQg@eQW{QIoRmAmmBgAclB_AemBa@ukA_@{s@w@mnA]gp@sAwzB}AapCkAihBe@i|@C{K?oKL{MX{MZiKr@{OhA{QlBsS~AkOxAiLpBoMnBgLnCcNdCcLvCoLzCuKpD}LbE{LhEkLrRmf@dI}R~H_StC}GzMq[xIySbIgSpIyUrFgQpFcRjEaQrD{OhEkSzDaT|CkRxBgOnB{OhB{P`BmQfBcTrAeTr@qQn@aR`@_RLiRAsQMqYMaQ_@mPg@kQw@mS{AaU{AgSiBwQ{AgOaCmR}CuS{DyTiEqTgEiR}DePkGyTaGcS}G_SeIcTiHePqJaTuKsTiO_]oQ}]eO}Z}IcSgDkJkDwKkEmNaDmLeCeKgCsKyE_YiAgJeC}RaAkK}@aLeCa[m@kRScPMoQUoe@]km@y@q{Ag@_bAaAmfBQaXUcWyAkoBuAihBmAmuAMe]Qcp@C}TBqTJoc@Hec@p@ifBA{hAa@}bAq@{o@y@ks@Yya@{@k~@_B{dBmB{tBo@icAY{n@WitAWuoAQ{kAUq|@O_rAk@ekCO}Zk@cq@aAoy@i@}`@cC{wByBwmBo@qe@UwWsAyeAaBivAqA_z@qCkeAeCcv@yG_kBcBef@gAsZ{DagAcDq_AmFc{AwBsl@_B}_@qAwd@aCybAqEodBeCm_AcC{`AiDupAmBqu@{@c_@cAe\\eAec@m@s]e@uZ]g[[ii@]{i@{@ghBc@_iAgAumBYor@_@ujAa@ky@i@{lAGiPy@wdBy@emBY{h@YcQi@}Ou@wRcAmRyAaVyCkc@mEcq@aC__@eAgQs@mOe@aNg@cSWaRWuMg@oSk@qq@QkQ}@}bAs@w|@GwP@iQRwR`@iRh@{Pr@wOjIc|AlCgf@x@{NxAgZz@}YZuOHiOF}OAeRSeW{@chA{@}hAa@_h@c@ce@Q}RMiq@K}Vg@{e@_AyhAU}Ng@kR}@uUUoGaAaT`@md@]wSs@i\\y@ic@JePf@gPl@kKr@}JfAwKtA}NjAqNTaIEwHe@yIyBm^eBiHqAcFaMci@iAoFmAwHcAuGSsBe@eFo@{J_@oIa@us@EeFaA}rBEqIMw`@KaRGmGYie@KkRsBqO]in@KwPKuMW_MAgK}Bgx@a@kYWgf@Mg]Yge@[gh@k@aqAm@ujASol@IcSCaIEsIAoCAu@EcII{Kk@o_@KoHKyFyA_f@]_d@nCsL^wMLoKAwOuCmzAw@cg@m@}^eFyxBcAsn@YsRe@g\\SwIQuGiAme@Q}Gk@mPBoEy@oYo@}TkDgoAiAkf@y@_^e@oSg@aUsAqk@}Ce}@{AyMoBwUyCcGg@qLa@sNeAka@y@q[aAw]{@mS`Q|G|@VzC|@lJnAlF\\hBLrJhAtC\\dRjCt\\rD|G|@lNpAvD\\nVhCbMz@jt@rDrETp\\`@~TGxECfGLlv@m@xd@GvSCpNGn[M~d@g@r\\InCArIIfJI|v@c@bQMvKEbOE|GQzDK~CDb`@KnN@vQLvIFxOEvTf@|REx@Cl\\XtBBnHFrY_@~MHdEAtRCpMAtKL~DHbG?zBAdB?~F?pD?tZAbI?hl@VxLFtQAp^AlD?dWBrNAhQ`@vABzI?zD@zB@t@?lL@|MFjP?xVBxE@bGFhK?|E?pJCvBA~D?zFIx@C`Rm@lDQjEWjM{@dL}@|_@{C`QgArGa@jHm@nMgAxHeAtJ{A`HiAxDi@zDy@~G}AdEaAvHkBfEmA`KsCdZwI~DiAxYoIvF]z@YfJ{C`IkClTiHzM{Gxm@}Z~@k@hKcFpBaAzBiAr@[rQkIdCmAbLiF`[oNlNwG|TiK|FmCbAg@bGqCfOcHhIwD`FqC~PcHdAc@jDeBvFsCdS_Kp^yR|NaKzDoChOwK\\WvL_JnKcIxFiElk@yb@b[eU`NuKzLyJhl@oe@dHgErGcDhH_DrI{ChMwCx@SfHoBrEVvZiC|e@eIdj@mM|RcI~KiHtEuChLwIp\\e]pMgRjM}TdMaZnGoRbQsj@~Xu~@vGqTbFuPhQko@`FmTtAkJ~BmOlDiPdJih@_G}EuRsGiBWwUmDqLa@k^bAeNw@qPkBwLuGiJ_NmD{Ky@wNdCuPrPcX~^_l@vNgd@rLo\\rImNdVgP`LuHzMyH",
                            }
                        ],
                        "summary": {
                            "has_time_restrictions": False,
                            "has_toll": False,
                            "has_highway": True,
                            "has_ferry": False,
                            "min_lat": 42.356887,
                            "min_lon": -83.275885,
                            "max_lat": 42.496507,
                            "max_lon": -82.869245,
                            "time": 2837.547,
                            "length": 54.324,
                            "cost": 4493.543,
                        },
                        "status_message": "Found route between points",
                        "status": 0,
                        "units": "kilometers",
                        "language": "en-US",
                    }
                }
            ],
            "id": "some_route",
        },
        "isochrones": {
            "type": "FeatureCollection",
            "bbox": [8.688474, 8.681829, 49.42577, 49.420176],
            "features": [
                {
                    "type": "Feature",
                    "properties": {
                        "group_index": 0,
                        "value": 100,
                        "center": [8.684162488752957, 49.4230724075398],
                    },
                    "geometry": {
                        "coordinates": [
                            [[8.684544, 49.423295], [8.684665, 49.423101], [8.684706, 49.423036]]
                        ],
                        "type": "Polygon",
                    },
                },
                {
                    "type": "Feature",
                    "properties": {
                        "group_index": 0,
                        "value": 100,
                        "center": [8.684162488752957, 49.4230724075398],
                    },
                    "geometry": {
                        "coordinates": [
                            [[8.684544, 49.423295], [8.684665, 49.423101], [8.684706, 49.423036]]
                        ],
                        "type": "Polygon",
                    },
                },
            ],
        },
        "matrix": {
            "sources_to_targets": [
                [{"distance": 0, "time": 0}, {"distance": 83.62, "time": 100}],
                [{"distance": 38.10, "time": 100}, {"distance": 0, "time": 0}],
            ]
        },
        "expansion": {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "LineString",
                        "coordinates": [[8.512978, 47.380938], [8.512694, 47.380651]],
                    },
                    "properties": {"duration": 0, "distance": 0, "cost": 0},
                },
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "LineString",
                        "coordinates": [[8.512694, 47.380651], [8.512589, 47.380545]],
                    },
                    "properties": {"duration": 4, "distance": 14, "cost": 8},
                },
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "LineString",
                        "coordinates": [[8.512694, 47.380651], [8.512978, 47.380938]],
                    },
                    "properties": {"duration": 7, "distance": 37, "cost": 8},
                },
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "LineString",
                        "coordinates": [[8.512978, 47.380938], [8.513163, 47.381124]],
                    },
                    "properties": {"duration": 11, "distance": 62, "cost": 14},
                },
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "LineString",
                        "coordinates": [[8.512589, 47.380545], [8.512461, 47.380427]],
                    },
                    "properties": {"duration": 7, "distance": 30, "cost": 16},
                },
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "LineString",
                        "coordinates": [[8.512461, 47.380427], [8.512249, 47.380203]],
                    },
                    "properties": {"duration": 15, "distance": 60, "cost": 28},
                },
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "LineString",
                        "coordinates": [[8.513163, 47.381124], [8.513588, 47.381568]],
                    },
                    "properties": {"duration": 23, "distance": 121, "cost": 28},
                },
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "LineString",
                        "coordinates": [[8.513588, 47.381568], [8.513632, 47.381613]],
                    },
                    "properties": {"duration": 24, "distance": 127, "cost": 35},
                },
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "LineString",
                        "coordinates": [[8.513632, 47.381613], [8.514038, 47.382042]],
                    },
                    "properties": {"duration": 34, "distance": 184, "cost": 48},
                },
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "LineString",
                        "coordinates": [[8.512249, 47.380203], [8.51156, 47.379499]],
                    },
                    "properties": {"duration": 33, "distance": 154, "cost": 49},
                },
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "LineString",
                        "coordinates": [[8.512978, 47.380938], [8.512871, 47.380983]],
                    },
                    "properties": {"duration": 17, "distance": 47, "cost": 644},
                },
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "LineString",
                        "coordinates": [[8.512871, 47.380983], [8.512795, 47.381015]],
                    },
                    "properties": {"duration": 21, "distance": 54, "cost": 663},
                },
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "LineString",
                        "coordinates": [[8.513632, 47.381613], [8.513528, 47.381658]],
                    },
                    "properties": {"duration": 31, "distance": 136, "cost": 667},
                },
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "LineString",
                        "coordinates": [[8.512795, 47.381015], [8.512679, 47.381069]],
                    },
                    "properties": {"duration": 27, "distance": 65, "cost": 673},
                },
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "LineString",
                        "coordinates": [[8.512679, 47.381069], [8.512116, 47.381319]],
                    },
                    "properties": {"duration": 56, "distance": 122, "cost": 712},
                },
            ],
            "properties": {"algorithm": "dijkstras"},
        },
        "trace_attributes": {
            "shape": "qekg}Aq|hqOhIvcBjHo@`]iCFnBbCSh@AlACz@CTCdCvc@vCnl@j@`PjAnTDp@HlBLrBBZpB`b@lBb]~AfZx@`MxWeEDv@FnAFzALz@f@Gt@GzPniBPrC|@Od@MvLgDdWmGjG{C~@v@TpB^?t@CjBMj@I@}@L]RQhAcAxCr@nCx@nCN~UpHrEv@rSrEbZhGFbV",
            "matched_points": [
                {
                    "distance_from_trace_point": 20.547,
                    "edge_index": 0,
                    "type": "matched",
                    "distance_along_edge": 0.000,
                    "lat": 49.420393,
                    "lon": 8.688601,
                },
                {
                    "distance_from_trace_point": 1.403,
                    "edge_index": 41,
                    "type": "matched",
                    "distance_along_edge": 0.435,
                    "lat": 49.415789,
                    "lon": 8.680916,
                },
            ],
            "edges": [
                {
                    "end_node": {
                        "transition_time": 0.000,
                        "fork": False,
                        "type": "street_intersection",
                        "admin_index": 0,
                        "elapsed_time": 83.294,
                        "time_zone": "Europe/Berlin",
                        "intersecting_edges": [
                            {
                                "road_class": "residential",
                                "use": "road",
                                "begin_heading": 353,
                                "to_edge_name_consistency": True,
                                "from_edge_name_consistency": False,
                                "driveability": "both",
                                "cyclability": "both",
                                "walkability": "both",
                            }
                        ],
                    },
                    "length": 0.118,
                    "speed": 5,
                    "road_class": "residential",
                    "begin_heading": 261,
                    "end_heading": 261,
                    "weighted_grade": 0.000,
                    "mean_elevation": 116,
                    "max_downward_grade": None,
                    "bicycle_network": 0,
                    "lane_count": 1,
                    "max_upward_grade": None,
                    "sidewalk": "both",
                    "density": 7,
                    "cycle_lane": "none",
                    "speed_limit": 30,
                    "truck_route": False,
                    "way_id": 25325392,
                    "pedestrian_type": "foot",
                    "end_shape_index": 1,
                    "id": 4649811837074,
                    "travel_mode": "pedestrian",
                    "surface": "paved_smooth",
                    "bridge": False,
                    "roundabout": False,
                    "drive_on_right": True,
                    "names": ["Roonstraße"],
                    "shoulder": False,
                    "sac_scale": 0,
                    "internal_intersection": False,
                    "tunnel": False,
                    "unpaved": False,
                    "use": "road",
                    "toll": False,
                    "traversability": "both",
                    "begin_shape_index": 0,
                },
                {
                    "end_node": {
                        "transition_time": 0.000,
                        "fork": False,
                        "type": "street_intersection",
                        "admin_index": 0,
                        "elapsed_time": 92.294,
                        "time_zone": "Europe/Berlin",
                        "intersecting_edges": [
                            {
                                "road_class": "service_other",
                                "use": "footway",
                                "begin_heading": 265,
                                "to_edge_name_consistency": False,
                                "from_edge_name_consistency": False,
                                "walkability": "both",
                            }
                        ],
                    },
                    "length": 0.017,
                    "speed": 7,
                    "road_class": "residential",
                    "begin_heading": 174,
                    "end_heading": 174,
                    "weighted_grade": -6.667,
                    "mean_elevation": 116,
                    "max_downward_grade": None,
                    "bicycle_network": 0,
                    "lane_count": 1,
                    "max_upward_grade": None,
                    "sidewalk": "both",
                    "density": 7,
                    "cycle_lane": "none",
                    "speed_limit": 30,
                    "truck_route": False,
                    "way_id": 52977975,
                    "pedestrian_type": "foot",
                    "end_shape_index": 2,
                    "id": 985500090514,
                    "travel_mode": "pedestrian",
                    "surface": "paved_smooth",
                    "bridge": False,
                    "roundabout": False,
                    "drive_on_right": True,
                    "names": ["Werderplatz"],
                    "shoulder": False,
                    "sac_scale": 0,
                    "internal_intersection": False,
                    "tunnel": False,
                    "unpaved": False,
                    "use": "road",
                    "toll": False,
                    "traversability": "both",
                    "begin_shape_index": 1,
                },
                {
                    "end_node": {
                        "transition_time": 0.000,
                        "fork": False,
                        "type": "street_intersection",
                        "admin_index": 0,
                        "elapsed_time": 130.412,
                        "time_zone": "Europe/Berlin",
                        "intersecting_edges": [
                            {
                                "road_class": "residential",
                                "use": "road",
                                "begin_heading": 173,
                                "to_edge_name_consistency": False,
                                "from_edge_name_consistency": True,
                                "driveability": "forward",
                                "cyclability": "forward",
                                "walkability": "both",
                            }
                        ],
                    },
                    "length": 0.054,
                    "speed": 5,
                    "road_class": "residential",
                    "begin_heading": 175,
                    "end_heading": 175,
                    "weighted_grade": 0.000,
                    "mean_elevation": 116,
                    "max_downward_grade": None,
                    "bicycle_network": 0,
                    "lane_count": 1,
                    "max_upward_grade": None,
                    "sidewalk": "both",
                    "density": 7,
                    "cycle_lane": "none",
                    "speed_limit": 30,
                    "truck_route": False,
                    "way_id": 52977975,
                    "pedestrian_type": "foot",
                    "end_shape_index": 3,
                    "id": 986070515858,
                    "travel_mode": "pedestrian",
                    "surface": "paved_smooth",
                    "bridge": False,
                    "roundabout": False,
                    "drive_on_right": True,
                    "names": ["Werderplatz"],
                    "shoulder": False,
                    "sac_scale": 0,
                    "internal_intersection": False,
                    "tunnel": False,
                    "unpaved": False,
                    "use": "road",
                    "toll": False,
                    "traversability": "both",
                    "begin_shape_index": 2,
                },
            ],
        },
        "optimized_route": {
            "trip": {
                "locations": [
                    {
                        "type": "break",
                        "lat": 49.420577,
                        "lon": 8.688641,
                        "side_of_street": "right",
                        "original_index": 0,
                    },
                    {"type": "through", "lat": 49.415776, "lon": 8.680916, "original_index": 1},
                    {"type": "through", "lat": 49.435776, "lon": 8.720916, "original_index": 2},
                    {
                        "type": "break",
                        "lat": 49.445776,
                        "lon": 8.780916,
                        "side_of_street": "left",
                        "original_index": 3,
                    },
                ],
                "legs": [
                    {
                        "summary": {
                            "has_time_restrictions": False,
                            "has_toll": False,
                            "has_highway": False,
                            "has_ferry": False,
                            "min_lat": 49.413745,
                            "min_lon": 8.677946,
                            "max_lat": 49.459559,
                            "max_lon": 8.780544,
                            "time": 11663.964,
                            "length": 21.476,
                            "cost": 21476.068,
                        },
                        "shape": "efkg}A_biqORlDhIvcBjHo@`]iC~Bg@`BObBOzYsCdRiBjM{ArAMrAKjb@yElSaAnDQdBWAjBI~NE|FI~LApD@jRIjj@H|O?bD?bCIbP?dT?X?j@Bpy@GbFOlLGhUCbNApEClLAbUEbB@~IpEJTBdK|At]rIj^dHhQdD`BDG`GHpVL~[JjD@~B`@t~@A~BEnBC`GNj~@rA\\fALvCd@lATfDl@Iub@Cqf@iC]mIwAiAU@_Ca@u~@A_CKkDWqs@FaGEoETi`AT_fADoD@uCNimBFcDByDa@ih@EgJGoGk@{r@GaHG}EaBomB_@{^C_EGcFe@{e@cAoz@CcDAy@?e@AuACgD{@u_AfMcA`a@gAzSc@pBEvBEv`@m@rFKnCBt@FtCb@D_CT{Cj@gI`D{a@oDg@{UeC{AUq@i@m@kA[kAKyBDoFTwIx@_Zd@ea@Kqt@?sQNwURmGR{DTyA`@_Bx@kCjByDx@iCTwAFaBAaBKiBSuCsAcKYwCSuCk@cJIwBe@ge@E_AIk@Si@W[[CUJQZGv@Ax@BjGJ`SA`AIt@mDpJoAnGi@rDmCbk@e@|Do@zB_AhAoAx@mBb@wBQaLaBjAwj@LiId@{Jj@}Jh@_JhAaUb@mKLwD@iGCyCSsAU{@g@kA]o@u@cAq@i@a@_@qA_Ak@]gBu@{A{@k@]e@c@o@cAcA_CeBiF]qAQ_AQmAQwBIoCYcHs@DmAeEqAuE_@{Aw@qCmAgFoDkN}CiM_@}A_AkEm@eCyAiF}AcF_@y@c@q@_@]c@a@OKgB[mAQuACy@B_BL_B\\aAb@m@f@e@n@_@v@Y`Aa@lBsApH{BdNaAtHkAnMyA|QqBvLqCzKuDhLq@eAMe@Og@WeBI{C|@wOzA{QXwLTcN\\wLb@eR^gO|@wIDoBM_Cm@oCsD{RyA_SiAcJyDwPiEqQmEmQaD_JwB}F_A_GiAqNuAuO_@oEyAkHaCaNuE{ZuKot@}BuOmBeM_A{GcCsOcDcQoA}IoA{HsAyKi@mD{@qCiC{GqBmDcC{BcCuBcByAsDoC_Aq@q@o@g@u@w@qAuBaEsGcMmHaLkAwAwAeBeJqHoGgIaJcFyHiFsIqF_BaBc@wAQ{ByJnCeIpBsVtB}HGsJ[aGkA_GiAiH}BcIuDyHuEoEqCwDkDeC{A{EoBoDaAkBg@{BWyAC{CBiBFaKj@gEGcCKqAO{EyAwEu@}DUcFE}C[qCk@_GiBoDm@oEg@yDEwGWkHo@yIeAcF_@wCEiHf@iDVwBB_CIwBUaJmByCm@aBm@yJcEwH}DoGsFqFoG{HiK{H}KyI}NgDoGw@wBeCiJoAmFaAuFgLa`@sJuRgJiX}AkEqAaF]iB[aBOwAK{AKsBAoDV}JLcDPeDPmBd@}Cn@kC~@}CxAqEfEuKnBcF`CgH~CeKtAsD`BeDfAeBxAmBrH{G~K{IbBoAdAkAn@oANo@L}@FiA?{@Gu@O}@Su@k@y@y@e@u@Eq@Lq@\\gIbGaGdDyBr@}Bb@mJvBgE|@cDdAeB~@uAv@eGbEaIdGqKjHmH|FgExCoDzCeBhBuAnB{BnDmIrMoE`H}Vh_@aA|AgBjCk@n@u@n@]ZkCtBa@yBsAqGkA}DkC{FqM_XgRs]wRi]yNeY_Pm`@}Nec@iJaa@iI}g@a@kCmBqO]gC[uCWmC_@sD\\eCNcBNcD@iDQiDc@mEm@{Es@kHs@aFyAqLcD_U}CmQiIua@}EwQyAqHyC{OaLwk@iDiQiBeJw@{Dw@yCk@eBmB_EqCkF{M_YuHiWw@uEe@yDW_FQeFAuFBsEFcDJmCJmBHwA_@_COaDByODwQNuM^aQh@aPTcF\\kF|Gcq@hD_e@ZsDb@uEfAcIbAiI~@wI\\{ENsEDgECmIGiHe@uHy@_I_BqJqAsJqDeXyDmYkBmJiK_c@cNul@}Dol@sFgBaBMcAl@o@v@y@~Ak@jBe@tCO`De@`ZmYfzFeCrZ}_@fwC`Arb@v@lPrBvQfBxK{PkB{HqAmIu@uJ{@tBbDfBrFjBrJf@pHJzEOjE_@lEc@`Cq@fD}ANqp@ByzAyNo`@sDsWaCsYeEm~@sQgXyDsK{AaFsAuGkC}MmHck@s^cLuHwG_EwFiCkGmBsGcAgFOyFIuc@t@oz@`AkYRw[iAe]_AcX`CsSjHcQnJy_@pTg[jSsUpQqLtEqAfAgArCdBr@dBh@zA\\pEv@vF|@rFt@jE^fBHzBB|Mc@dN}@xOiAjBKfB?xA@|AHlAJtBZhDp@fJjCtJ`DxNzFbEfBpAx@n@j@f@n@Xv@Tz@LrACfAKt@]tAo@`B_EhI_BfD}@~CaAfDcE~PgEnRsApGgAzG}CzVeBlPrDuFnJuRnFsIzAcBrAoAbEiChFaDjF{BxDkAjE{@xDa@hB@rANjAX|@`@`BnAdC|ChGzGzFtFzMxLpFbF`F`F|BzB~ApBzE~GhEhFbDhDjVpUrN|MvEtDtVjPdCtBtArAjAnAxAvBrEnJ~DxIdA~BjA`E|@zErAhKz@`FbBjH|AzFzDjL`C~FbDhGjDbFbDfD~BfBxDrA~Cf@fEFrDKlEm@vDqAxC}AzK}GvKaIvMiHvMqE~McEfIeB|FiApFQpID`E@fF^jD`AzDdBjE~CdIbHfGlGtF|HnPj]tCrGtCfIrEbQ`Mbe@r@xBfAfCfBhDxAdBlAz@n@Xv@PbABx@Mr@W|@i@~AiBrCcEpEuK~DsP|CgNfEiNtFyNnRkj@fTe]vTiRx@s@hCeCxAuBv@sAv@}@z@g@pA_@rAMpBFpBf@jChAvBpAbKlGzJxH`IjJfIpLlIfMvDlF`BnBbClB|BfAfFnBjA`An@|@`@`APfA@hAIz@Ur@a@~@Yd@Xe@`@_ATs@H{@AiAQgAa@aAo@}@kAaAgFoB}BgAcCmBaBoBwDmFmIgMgIqLaIkJ{JyHcKmGwBqAkCiAqBg@qBGsALqA^{@f@w@|@w@rAyAtBiCdCqV|SgTd]oRjj@uFxNgEhN}CfN_ErPqEtKsCbE_BhB}@h@s@Vy@LcACw@Qo@YmA{@yAeBgBiDgAgCs@yBaMce@sEcQuCgIuCsGoPk]uF}HgGmGeIcHkE_D{DeBkDaAgF_@aEAqIEqFP}FhAgIdB_NbEwMpEwMhHwK`I{K|GyC|AwDpAmEl@sDJgEG_Dg@yDsA_CgBcDgDkDcFcDiGaC_G{DkL}A{FcBkH{@aFsAiK}@{EkAaEeA_C_EyIsEoJyAwBkAoAuAsAeCuBuVkPwEuDsN}MkVqUcDiDiEiF{E_H_BqB}B{BaFaFqFcF{MyL{FuFiG{GeC}CaBoA}@a@kAYsAOiBAyD`@kEz@yDjAkFzBiF`DcEhCsAnA{AbBoFrIoJtRsDtFdBmP|C{VfA{GrAqGfEoRbE_Q`AgD|@_D~AgD~DiIn@aB\\uAJu@BgAMsAU{@Yw@g@o@o@k@qAy@cEgByN{FuJaDgJkCiDq@uB[mAK}AIyAAgB?kBJyOhAeN|@}Mb@{BCgBIkE_@sFu@wF}@qEw@{A]eBi@eBs@}@EcEtAoCz@aJjDoC~@qElAmFlA}JlA{Fv@eRfCcYlEgUzCoTzCuQt@_PQso@}G{EgBoKqD_YqJy`@qd@{a@st@{Sk_AgNozBgBwY[_DqB_T_Fe_@qJid@aG_VgMmd@s_@sdA_M_n@gd@ghB{EaQcBoIuAwIg@qFe@uJMkUVaKvC_`@pA_XtAcz@x@aRjBoXZqGHoJ[gGyE{a@a@_HwBuA}Ae@kCaCoCwDuJkR{Zeq@mf@_r@us@qz@}CmHeD}IsCgLw@qHQiIp@cV~@kUvDor@vAqXxBe\\dG_s@jFei@nCmYl@iEf@wDHaBJuBEaC]}Bs@qFaCyNi@iDUwDB_FaAoHgB}MuBsN}CwQoCyUsB{QoEgc@aBo^yA}^LkXnI{_@zOy]zYsk@zZ_t@~`@g{@r\\up@pO{_@jHyW|EkT|FkW~DqQpA{FKyCC{CCmC?aA?kBT}y@p@kc@v@wO`ByI~CiJxLk[je@whApZqv@jSab@dNq]`MkXhCcLTqEGkGWoLeAm`@g@q[]}Y]cJa@eUe@qNqAwOvBqDfM_T`L{Lb_@ob@ba@gj@b_@ad@`T_P`m@{Ufa@hCdm@jKnQbHzM`ClPaG`LoLlLuRpFsPw@wJ{BwLqHcSsOwUgXoTmWj@{a@jH}Q`@{P_Bea@qJuI{E}EgFaH{SmEqScIoWiVgf@iKsSnOzDhXxUlIvMdRzYpVjLnOkDxTkLpV{]hJwQ`SmLlPwMpOwIhX?nd@`CbYmLdRmTvi@st@he@{]z\\eP",
                    }
                ],
                "summary": {
                    "has_time_restrictions": False,
                    "has_toll": False,
                    "has_highway": False,
                    "has_ferry": False,
                    "min_lat": 49.413745,
                    "min_lon": 8.677946,
                    "max_lat": 49.459559,
                    "max_lon": 8.780544,
                    "time": 11663.964,
                    "length": 21.476,
                    "cost": 21476.068,
                },
                "status_message": "Found route between points",
                "status": 0,
                "units": "kilometers",
                "language": "en-US",
            }
        },
    },
    "osrm": {
        "directions_geojson": {
            "routes": [
                {
                    "geometry": {"coordinates": [[8.681495, 49.41461], [8.681445, 49.415755]]},
                    "duration": 100,
                    "distance": 100,
                }
            ]
        },
        "directions_polyline": {
            "routes": [
                {
                    "geometry": "qmbjHspkr@kCmCpE{T~M|@|QcRvC}OjCgD~F~@~I~SjLxqAjT||@lDde@aBhh@uUbuAmJpPod@|c@iWhQoSt_@}Hx]oTfNqNWqQeKilAa]hByx@DiCvDd@dNxJ[zMl[eCfKlBn[rUb]z]pGoGbHtY|j@xw@jKnFfd@~IdhEpyFm@rGpInKyAhDuDuE",
                    "duration": 100,
                    "distance": 100,
                }
            ]
        },
        "directions_polyline6": {
            "routes": [
                {
                    "geometry": "wpan|A}n|`O{j@yk@v`AuyE~tCfRx|De~Dln@khDhj@as@doAnR~lBhqEtdCxzXvtExjRvu@t|Ju]z{K}aFd|YiqBrnDkvJrpJ_rF|uDalEhfIibB`sHavEjwCgzCyFayDkxBadWykHf`@_aQ|@cj@rx@rJjvCduBgGtsCb{Gsh@lyBla@f|GhaFxkHvsHttAatAhzAliGvvLnwPtzBriAjsJhmBvz}@jhmAoMnuA`iBb|Bi[bt@}w@ebA",
                    "duration": 100,
                    "distance": 100,
                }
            ]
        },
        "matrix": {"durations": [[1, 2, 3], [4, 5, 6]], "distances": [[1, 2, 3], [4, 5, 6]]},
    },
    "mapbox_osrm": {
        "directions": {
            "routes": [
                {
                    "geometry": {"coordinates": [[8.681495, 49.41461], [8.681445, 49.415755]]},
                    "duration": 100,
                    "distance": 100,
                }
            ]
        },
        "isochrones": {
            "type": "FeatureCollection",
            "bbox": [8.688474, 8.681829, 49.42577, 49.420176],
            "features": [
                {
                    "type": "Feature",
                    "properties": {
                        "group_index": 0,
                        "value": 100,
                        "center": [8.684162488752957, 49.4230724075398],
                    },
                    "geometry": {
                        "coordinates": [
                            [[8.684544, 49.423295], [8.684665, 49.423101], [8.684706, 49.423036]]
                        ],
                        "type": "Polygon",
                    },
                },
                {
                    "type": "Feature",
                    "properties": {
                        "group_index": 0,
                        "value": 100,
                        "center": [8.684162488752957, 49.4230724075398],
                    },
                    "geometry": {
                        "coordinates": [
                            [[8.684544, 49.423295], [8.684665, 49.423101], [8.684706, 49.423036]]
                        ],
                        "type": "Polygon",
                    },
                },
            ],
        },
        "matrix": {"distances": [[1, 2, 3], [4, 5, 6]], "durations": [[1, 2, 3], [4, 5, 6]]},
    },
    "google": {
        "directions": {
            "routes": [
                {
                    "legs": [
                        {
                            "distance": {"value": 541359},
                            "duration": {"value": 19448},
                            "steps": [
                                {
                                    "distance": {"value": 280},
                                    "duration": {"value": 67},
                                    "polyline": {
                                        "points": "ayotGvy_sMV]t@_APk@DOFW@O@OAwADiE?k@Hq@@UHuG@s@@{@DiIDsFDkG@aIAa@?WAUASGe@Im@EYEOCOO_@Kk@Ie@Oe@GWKUMWwAoCmDmGwB}D_AgBoAaCqCaGuA_D}@_BIS]m@KQMUy@}AwAgCk@cAiB_D{AsCcBwCmAsBm@aAoAuBeB{Bm@sAe@mAMa@Qi@Uy@e@eB[eAIUOm@u@iCi@eCaA}DcAyCy@qB{EiIMU"
                                    },
                                },
                                {
                                    "distance": {"value": 2493},
                                    "duration": {"value": 511},
                                    "polyline": {
                                        "points": "ayotGvy_sMV]t@_APk@DOFW@O@OAwADiE?k@Hq@@UHuG@s@@{@DiIDsFDkG@aIAa@?WAUASGe@Im@EYEOCOO_@Kk@Ie@Oe@GWKUMWwAoCmDmGwB}D_AgBoAaCqCaGuA_D}@_BIS]m@KQMUy@}AwAgCk@cAiB_D{AsCcBwCmAsBm@aAoAuBeB{Bm@sAe@mAMa@Qi@Uy@e@eB[eAIUOm@u@iCi@eCaA}DcAyCy@qB{EiIMU"
                                    },
                                },
                            ],
                        }
                    ]
                }
            ],
            "status": "OK",
        },
        "matrix": {
            "rows": [
                {
                    "elements": [
                        {
                            "status": "OK",
                            "distance": {"text": "225 mi", "value": 361957},
                            "duration": {"text": "3 hours 50 mins", "value": 13813},
                        }
                    ]
                }
            ]
        },
    },
    "otp_v2": {
        "directions": {
            "data": {
                "plan": {
                    "itineraries": [
                        {
                            "duration": 178,
                            "legs": [
                                {
                                    "duration": 178.0,
                                    "distance": 1073.17,
                                    "legGeometry": {
                                        "points": "olslHg_`t@@N`@bI\\E~AMJAJAF?tAKjBSFAFApBY~@EPAHA?P?j@AV?l@?P?|@AhC@t@?P?JAt@?bA@bEATAj@?jC?h@AfA?H?`@T@@?d@H`B`@dB\\v@NJ??X?jA"
                                    },
                                }
                            ],
                        }
                    ]
                }
            }
        },
        "isochrones": {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "properties": {"time": "1200"},
                    "geometry": {
                        "type": "MultiPolygon",
                        "coordinates": [
                            [
                                [
                                    [8.3366, 48.2268],
                                    [8.338, 48.226],
                                    [8.3381, 48.226],
                                    [8.3407, 48.227],
                                    [8.3417, 48.2266],
                                    [8.343, 48.226],
                                    [8.3431, 48.2258],
                                    [8.3434, 48.2258],
                                    [8.3451, 48.2253],
                                    [8.3461, 48.225],
                                    [8.3474, 48.225],
                                    [8.3488, 48.225],
                                    [8.3499, 48.226],
                                    [8.3515, 48.2269],
                                    [8.3521, 48.2278],
                                    [8.3542, 48.2294],
                                    [8.3554, 48.2296],
                                    [8.3547, 48.2299],
                                    [8.3551, 48.2314],
                                    [8.3557, 48.2324],
                                    [8.3555, 48.2332],
                                    [8.3548, 48.2335],
                                    [8.3542, 48.2344],
                                    [8.3537, 48.2346],
                                    [8.3529, 48.235],
                                    [8.353, 48.236],
                                    [8.3532, 48.2368],
                                    [8.3533, 48.2379],
                                    [8.3538, 48.2386],
                                    [8.3526, 48.2393],
                                    [8.3519, 48.2404],
                                    [8.3517, 48.2405],
                                    [8.3515, 48.2406],
                                    [8.3489, 48.2405],
                                    [8.3488, 48.2404],
                                    [8.3486, 48.2404],
                                    [8.3463, 48.2387],
                                    [8.3462, 48.2386],
                                    [8.3461, 48.2385],
                                    [8.346, 48.2385],
                                    [8.3458, 48.2386],
                                    [8.3447, 48.2394],
                                    [8.3434, 48.2392],
                                    [8.3415, 48.2386],
                                    [8.3407, 48.2385],
                                    [8.3405, 48.2385],
                                    [8.3404, 48.2386],
                                    [8.3401, 48.24],
                                    [8.3384, 48.2404],
                                    [8.3382, 48.2405],
                                    [8.338, 48.2407],
                                    [8.3375, 48.2419],
                                    [8.3366, 48.2422],
                                    [8.3369, 48.2432],
                                    [8.3353, 48.2435],
                                    [8.3346, 48.2435],
                                    [8.3326, 48.2423],
                                    [8.3307, 48.2422],
                                    [8.3325, 48.2421],
                                    [8.3317, 48.2404],
                                    [8.3306, 48.239],
                                    [8.3315, 48.2386],
                                    [8.3323, 48.2383],
                                    [8.3326, 48.2373],
                                    [8.3329, 48.2369],
                                    [8.3329, 48.2368],
                                    [8.3339, 48.2358],
                                    [8.3342, 48.235],
                                    [8.3338, 48.2339],
                                    [8.3353, 48.2338],
                                    [8.3357, 48.2334],
                                    [8.3357, 48.2332],
                                    [8.3359, 48.2317],
                                    [8.3365, 48.2314],
                                    [8.3353, 48.2298],
                                    [8.335, 48.2296],
                                    [8.335, 48.2294],
                                    [8.3353, 48.2286],
                                    [8.3356, 48.228],
                                    [8.3359, 48.2278],
                                    [8.3366, 48.2268],
                                ]
                            ]
                        ],
                    },
                    "id": "fid--1f71e282_18930eaafe4_-7fe3",
                },
                {
                    "type": "Feature",
                    "properties": {"time": "600"},
                    "geometry": {
                        "type": "MultiPolygon",
                        "coordinates": [
                            [
                                [
                                    [8.3405, 48.233],
                                    [8.3407, 48.2328],
                                    [8.342, 48.2322],
                                    [8.3434, 48.2315],
                                    [8.3437, 48.2316],
                                    [8.3461, 48.2322],
                                    [8.3486, 48.2332],
                                    [8.3478, 48.2343],
                                    [8.3468, 48.235],
                                    [8.3465, 48.2352],
                                    [8.3461, 48.2351],
                                    [8.3446, 48.2357],
                                    [8.3434, 48.2356],
                                    [8.3411, 48.235],
                                    [8.3407, 48.2342],
                                    [8.3403, 48.2332],
                                    [8.3405, 48.233],
                                ]
                            ]
                        ],
                    },
                    "id": "fid--1f71e282_18930eaafe4_-7fe4",
                },
            ],
        },
    },
    "ors": {
        "directions": {
            "json": {
                "routes": [
                    {
                        "summary": {"distance": 2439, "duration": 100},
                        "geometry": "ihrlHir~s@cFFcAKeB_@_B]g@IUAQB]PaCr@y@cJeBXe@qJ_@kH??",
                    }
                ]
            },
            "geojson": {
                "type": "FeatureCollection",
                "features": [
                    {
                        "type": "Feature",
                        "geometry": {
                            "coordinates": [[8.681495, 49.41461], [8.681445, 49.415755]],
                            "type": "LineString",
                        },
                        "properties": {"summary": {"distance": 850.5, "duration": 191.4}},
                    }
                ],
            },
        },
        "isochrones": {
            "type": "FeatureCollection",
            "bbox": [8.688474, 8.681829, 49.42577, 49.420176],
            "features": [
                {
                    "type": "Feature",
                    "properties": {
                        "group_index": 0,
                        "value": 100,
                        "center": [8.684162488752957, 49.4230724075398],
                    },
                    "geometry": {
                        "coordinates": [
                            [[8.684544, 49.423295], [8.684665, 49.423101], [8.684706, 49.423036]]
                        ],
                        "type": "Polygon",
                    },
                },
                {
                    "type": "Feature",
                    "properties": {
                        "group_index": 0,
                        "value": 200,
                        "center": [8.684162488752957, 49.4230724075398],
                    },
                    "geometry": {
                        "coordinates": [
                            [[8.683974, 49.423982], [8.684035, 49.423627], [8.685104, 49.422131]]
                        ],
                        "type": "Polygon",
                    },
                },
                {
                    "type": "Feature",
                    "properties": {
                        "group_index": 0,
                        "value": 300,
                        "center": [8.684162488752957, 49.4230724075398],
                    },
                    "geometry": {
                        "coordinates": [
                            [[8.68261, 49.423744], [8.682671, 49.423389], [8.683764, 49.421902]]
                        ],
                        "type": "Polygon",
                    },
                },
                {
                    "type": "Feature",
                    "properties": {
                        "group_index": 0,
                        "value": 400,
                        "center": [8.684162488752957, 49.4230724075398],
                    },
                    "geometry": {
                        "coordinates": [
                            [[8.681829, 49.424426], [8.682416, 49.421699], [8.686179, 49.420176]]
                        ],
                        "type": "Polygon",
                    },
                },
            ],
        },
        "matrix": {
            "durations": [[7900.34], [0], [136841.92], [483295.5]],
            "distances": [[125.58], [0], [238.25], [100]],
        },
    },
    "graphhopper": {
        "directions": {
            "paths": [
                {"distance": 15239.553, "time": 2349463, "points": "korlHun~s@inUAiBP"},
                {"distance": 15239.553, "time": 2349463, "points": "korlHun~s@inUAiBP"},
                {"distance": 15239.553, "time": 2349463, "points": "korlHun~s@inUAiBP"},
            ]
        },
        "isochrones": {
            "polygons": [
                {
                    "type": "Feature",
                    "properties": {"bucket": 0},
                    "geometry": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [8.345841896068496, 48.23514181901086, 1.0],
                                [8.340545650732793, 48.23651784814562, 1.5],
                                [8.340935036709944, 48.23593307068795, 1.5],
                            ]
                        ],
                    },
                },
                {
                    "type": "Feature",
                    "properties": {"bucket": 1},
                    "geometry": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [8.345999848380682, 48.23155678581201, 2.0],
                                [8.348431345412836, 48.234402721399135, 2.0],
                                [8.348099422039823, 48.23458791489723, 2.0],
                            ]
                        ],
                    },
                },
                {
                    "type": "Feature",
                    "properties": {"bucket": 2},
                    "geometry": {
                        "type": "Polygon",
                        "coordinates": [
                            [
                                [8.349068835729408, 48.2354851976518, 2.5],
                                [8.34836307396443, 48.23601708826144],
                                [8.342155162442218, 48.23711268388732, 2.5],
                            ]
                        ],
                    },
                },
            ]
        },
        "matrix": {
            "distances": [[0, 1181, 13965], [1075, 0, 14059], [14120, 13766, 0]],
            "times": [[0, 255, 2122], [242, 0, 2094], [2144, 2021, 0]],
            "weights": [[0.0, 272.99, 2331.526], [258.115, 0.0, 2305.121], [2356.307, 2225.083, 0.0]],
        },
    },
}

ENDPOINTS_QUERIES = {
    "google": {
        "directions": {
            "profile": "driving",
            "locations": PARAM_LINE_MULTI,
            "alternatives": True,
            "avoid": ["tolls", "ferries"],
            "optimize": False,
            "language": "de",
            "region": "de",
            "units": "metrics",
            "arrival_time": 1567512000,
            "traffic_model": "optimistic",
            "transit_mode": ["bus", "rail"],
            "transit_routing_preference": "less_walking",
        },
        "matrix": {
            "profile": "driving",
            "locations": PARAM_LINE_MULTI,
            "avoid": ["tolls", "ferries"],
            "language": "de",
            "region": "de",
            "units": "metrics",
            "arrival_time": 1567512000,
            "traffic_model": "optimistic",
            "transit_mode": ["bus", "rail"],
            "transit_routing_preference": "less_walking",
        },
    },
    "osrm": {
        "directions": {
            "profile": "driving",
            "locations": PARAM_LINE_MULTI,
            "radiuses": [PARAM_INT_BIG, PARAM_INT_BIG, PARAM_INT_BIG],
            "bearings": [[PARAM_INT_SMALL, PARAM_INT_SMALL]] * 3,
            "alternatives": True,
            "steps": True,
            "annotations": True,
            "geometries": "geojson",
            "overview": "simplified",
            "continue_straight": True,
        },
        "matrix": {
            "profile": "walking",
            "locations": PARAM_LINE_MULTI,
            "radiuses": [PARAM_INT_BIG, PARAM_INT_BIG, PARAM_INT_BIG],
            "bearings": [[PARAM_INT_SMALL, PARAM_INT_SMALL]] * 3,
            "annotations": ["distance", "duration"],
        },
    },
    "mapbox_osrm": {
        "directions": {
            "locations": PARAM_LINE_MULTI,
            "profile": "driving",
            "radiuses": [PARAM_INT_BIG, PARAM_INT_BIG, PARAM_INT_BIG],
            "bearings": [[PARAM_INT_SMALL, PARAM_INT_SMALL]] * 3,
            "alternatives": 3,
            "steps": True,
            "annotations": ["duration", "distance", "speed"],
            "geometries": "geojson",
            "overview": "simplified",
            "continue_straight": True,
            "exclude": "motorway",
            "approaches": ["curb"] * 3,
            "banner_instructions": True,
            "language": "de",
            "roundabout_exits": True,
            "voice_instructions": True,
            "voice_units": "metric",
            "waypoint_names": ["a", "b", "c"],
            "waypoint_targets": PARAM_LINE_MULTI,
        },
        "isochrones": {
            "locations": PARAM_POINT,
            "profile": "driving",
            "intervals": [600, 1200],
            "contours_colors": ["ff0000", "00FF00"],
            "polygons": True,
            "generalize": 0.5,
            "denoise": 0.1,
        },
        "matrix": {
            "locations": PARAM_LINE_MULTI,
            "profile": "driving",
            "annotations": ["distance", "duration"],
            "fallback_speed": PARAM_INT_SMALL,
        },
    },
    "graphhopper": {
        "directions": {
            "locations": PARAM_LINE_MULTI,
            "profile": "car",
            "elevation": True,
            "points_encoded": True,
            "format": "json",
            "instructions": False,
            "locale": "en",
            "calc_points": False,
            "optimize": True,
            "debug": True,
            "point_hints": ["OSM Street", "Graphhopper Lane", "Routing Broadway"],
            "snap_preventions": ["trunk", "ferry"],
            "curbsides": ["any", "right"],
            "turn_costs": True,
            "details": ["tolls", "time"],
            "ch_disable": True,
            "custom_model": {
                "speed": [
                    {
                        "if": "true",
                        "limit_to": "100",
                    },
                ],
                "priority": [
                    {
                        "if": "road_class == MOTORWAY",
                        "multiply_by": "0",
                    },
                ],
                "distance_influence": 100,
            },
            "heading": [PARAM_INT_SMALL, PARAM_INT_SMALL, PARAM_INT_SMALL],
            "heading_penalty": 100,
            "pass_through": True,
            "algorithm": "alternative_route",
            "round_trip_distance": 10000,
            "round_trip_seed": 3,
            "alternative_route_max_paths": 2,
            "alternative_route_max_weight_factor": 1.7,
            "alternative_route_max_share_factor": 0.7,
        },
        "matrix": {
            "locations": PARAM_LINE_MULTI,
            "profile": "car",
            "out_array": ["weights", "times", "distances"],
            "debug": True,
        },
        "isochrones": {
            "locations": PARAM_POINT,
            "profile": "car",
            "intervals": [1000],
            "buckets": 5,
            "reverse_flow": True,
            "debug": False,
        },
    },
    "valhalla": {
        "directions": {
            "locations": PARAM_LINE_MULTI,
            "options": {
                "maneuver_penalty": PARAM_INT_SMALL,
                "toll_booth_cost": PARAM_INT_SMALL,
                "country_crossing_penalty": PARAM_INT_SMALL,
            },
            "profile": "auto",
            "preference": "shortest",
            "directions_type": "none",
            "avoid_locations": PARAM_POINT,
            "avoid_polygons": PARAM_POLY,
            "date_time": {"type": 1, "value": "2021-03-03T08:06"},
            "language": "pirate",
            "instructions": False,
            "id": "wacko",
            "somerandom": "option",
            "units": "kilometers",
        },
        "optimized_route": {
            "locations": PARAM_LINE_OPTIMIZED,
            "options": {
                "maneuver_penalty": PARAM_INT_SMALL,
                "toll_booth_cost": PARAM_INT_SMALL,
                "country_crossing_penalty": PARAM_INT_SMALL,
            },
            "profile": "auto",
            "preference": "shortest",
            "directions_type": "none",
            "avoid_locations": PARAM_POINT,
            "avoid_polygons": PARAM_POLY,
            "date_time": {"type": 1, "value": "2021-03-03T08:06"},
            "language": "pirate",
            "instructions": False,
            "id": "wacko2",
            "somerandom": "option",
            "units": "kilometers",
        },
        "alternatives": {
            "locations": [[-83.271400, 42.358528], [-82.749855, 42.43892]],
            "profile": "auto",
            "id": "some_route",
            "alternatives": 1,
        },
        "isochrones": {
            "locations": PARAM_POINT,
            "options": {
                "maneuver_penalty": PARAM_INT_SMALL,
                "toll_booth_cost": PARAM_INT_SMALL,
                "country_crossing_penalty": PARAM_INT_SMALL,
            },
            "profile": "auto",
            "id": "wacko",
            "preference": "shortest",
            "intervals": [600, 1200],
            "colors": ["ff0000", "00FF00"],
            "polygons": True,
            "avoid_locations": PARAM_POINT,
            "generalize": 0.5,
            "denoise": 0.1,
            "date_time": {"type": 1, "value": "2021-03-03T08:06"},
        },
        "matrix": {
            "locations": PARAM_LINE_MULTI,
            "options": {
                "maneuver_penalty": PARAM_INT_SMALL,
                "toll_booth_cost": PARAM_INT_SMALL,
                "country_crossing_penalty": PARAM_INT_SMALL,
            },
            "avoid_locations": PARAM_POINT,
            "profile": "auto",
            "units": "kilometers",
            "id": "wacko",
            "preference": "shortest",
        },
        "expansion": {
            "expansion_properties": ["distance", "duration", "cost"],
            "intervals": [30],
            "locations": [(8.512516, 47.380742)],
            "profile": "auto",
        },
        "trace_attributes": {
            "locations": PARAM_LINE_MULTI,
            "profile": "pedestrian",
            "shape_match": "map_snap",
            "filters": ["edge.id", "matched.type"],
            "filters_action": "exclude",
            "options": {
                "maneuver_penalty": PARAM_INT_SMALL,
                "toll_booth_cost": PARAM_INT_SMALL,
                "country_crossing_penalty": PARAM_INT_SMALL,
            },
        },
    },
    "otp_v2": {
        "directions": {
            "locations": PARAM_LINE,
            "profile": "CAR",
            "num_itineraries": 1,
        },
        "directions_alternative": {
            "locations": PARAM_LINE,
            "profile": "CAR",
            "num_itineraries": 3,
        },
        "isochrones": {
            "locations": PARAM_POINT,
            "time": datetime.datetime.fromisoformat("2023-07-07T16:00:00+00:00"),
            "profile": "WALK,TRANSIT",
            "cutoffs": [600, 1200],
        },
        "raster": {
            "locations": PARAM_POINT,
            "time": datetime.datetime.fromisoformat("2023-07-07T16:00:00+00:00"),
            "profile": "WALK,TRANSIT",
            "cutoff": 1200,
        },
    },
    "ors": {
        "directions": {
            "locations": PARAM_LINE,
            "profile": "driving-car",
            "preference": "fastest",
            "language": "en",
            "geometry": "true",
            "geometry_simplify": "False",
            "instructions": "False",
            "instructions_format": "html",
            "roundabout_exits": "true",
            "attributes": ["avgspeed"],
            "radiuses": [PARAM_INT_SMALL] * 2,
            "bearings": [[PARAM_INT_SMALL, PARAM_INT_SMALL]] * 2,
            "elevation": "true",
            "extra_info": ["roadaccessrestrictions"],
            "options": {"avoid_features": ["highways", "tollways"]},
        },
        "isochrones": {
            "locations": PARAM_POINT,
            "profile": "cycling-regular",
            "interval_type": "distance",
            "intervals": [PARAM_INT_BIG],
            "location_type": "destination",
            "attributes": ["area", "reachfactor"],
        },
        "matrix": {
            "locations": PARAM_LINE,
            "sources": [1],
            "destinations": [0],
            "profile": "driving-car",
            "metrics": ["duration", "distance"],
            "resolve_locations": "true",
        },
    },
}

ENDPOINTS_EXPECTED = {
    "valhalla": {
        "directions": {
            "locations": [
                {"lat": 49.420577, "lon": 8.688641},
                {"lat": 49.415776, "lon": 8.680916},
                {"lat": 49.445776, "lon": 8.780916},
            ],
            "costing": "auto",
            "costing_options": {
                "auto": {
                    "maneuver_penalty": 50,
                    "toll_booth_cost": 50,
                    "country_crossing_penalty": 50,
                    "shortest": True,
                }
            },
            "directions_options": {"language": "pirate", "directions_type": "none"},
            "avoid_locations": [{"lon": 8.34234, "lat": 48.23424}],
            "avoid_polygons": PARAM_POLY,
            "date_time": {"type": 1, "value": "2021-03-03T08:06"},
            "id": "wacko",
            "narrative": False,
            "somerandom": "option",
            "units": "kilometers",
        },
        "alternatives": {
            "locations": [{"lat": 42.358528, "lon": -83.271400}, {"lat": 42.43892, "lon": -82.749855}],
            "costing": "auto",
            "units": "kilometers",
            "id": "some_route",
            "narrative": False,
            "alternates": 1,
        },
        "isochrones": {
            "locations": [{"lat": PARAM_POINT[1], "lon": PARAM_POINT[0]}],
            "costing": "auto",
            "costing_options": {
                "auto": {
                    "maneuver_penalty": 50,
                    "toll_booth_cost": 50,
                    "country_crossing_penalty": 50,
                    "shortest": True,
                }
            },
            "contours": [{"time": 10, "color": "ff0000"}, {"time": 20, "color": "00FF00"}],
            "avoid_locations": [{"lon": 8.34234, "lat": 48.23424}],
            "date_time": {"type": 1, "value": "2021-03-03T08:06"},
            "id": "wacko",
            "denoise": 0.1,
            "polygons": True,
            "generalize": 0.5,
        },
        "matrix": {
            "sources": [
                {"lat": 49.420577, "lon": 8.688641},
                {"lat": 49.415776, "lon": 8.680916},
                {"lat": 49.445776, "lon": 8.780916},
            ],
            "targets": [
                {"lat": 49.420577, "lon": 8.688641},
                {"lat": 49.415776, "lon": 8.680916},
                {"lat": 49.445776, "lon": 8.780916},
            ],
            "costing": "auto",
            "costing_options": {
                "auto": {
                    "maneuver_penalty": 50,
                    "toll_booth_cost": 50,
                    "country_crossing_penalty": 50,
                    "shortest": True,
                }
            },
            "avoid_locations": [{"lon": 8.34234, "lat": 48.23424}],
            "id": "wacko",
            "units": "kilometers",
        },
        "expansion": {
            "expansion_properties": ["distance", "duration", "cost"],
            "contours": [{"time": 0.5}],
            "locations": [{"lon": 8.512516, "lat": 47.380742}],
            "costing": "auto",
            "action": "isochrone",
        },
        "trace_attributes": {
            "shape": [
                {"lat": 49.420577, "lon": 8.688641},
                {"lat": 49.415776, "lon": 8.680916},
                {"lat": 49.445776, "lon": 8.780916},
            ],
            "costing": "pedestrian",
            "shape_match": "map_snap",
            "filters": {"attributes": ["edge.id", "matched.type"]},
            "action": "exclude",
            "costing_options": {
                "pedestrian": {
                    "maneuver_penalty": PARAM_INT_SMALL,
                    "toll_booth_cost": PARAM_INT_SMALL,
                    "country_crossing_penalty": PARAM_INT_SMALL,
                }
            },
        },
        "optimized_route": {
            "costing": "auto",
            "narrative": False,
            "locations": [
                {"lon": 8.688641, "lat": 49.420577},
                {"lon": 8.680916, "lat": 49.415776},
                {"lon": 8.720916, "lat": 49.435776},
                {"lon": 8.780916, "lat": 49.445776},
            ],
            "costing_options": {
                "auto": {
                    "maneuver_penalty": 50,
                    "toll_booth_cost": 50,
                    "country_crossing_penalty": 50,
                    "shortest": True,
                }
            },
            "directions_options": {"language": "pirate", "directions_type": "none"},
            "avoid_locations": [{"lon": 8.34234, "lat": 48.23424}],
            "avoid_polygons": [[[8.688641, 49.420577], [8.680916, 49.415776]]],
            "date_time": {"type": 1, "value": "2021-03-03T08:06"},
            "id": "wacko2",
            "somerandom": "option",
            "units": "kilometers",
        },
    },
    "graphhopper": {
        "directions": {
            "profile": "car",
            "points": [[8.688641, 49.420577], [8.680916, 49.415776], [8.780916, 49.445776]],
            "type": "json",
            "optimize": True,
            "instructions": False,
            "locale": "en",
            "elevation": True,
            "points_encoded": True,
            "calc_points": False,
            "debug": True,
            "point_hints": ["OSM Street", "Graphhopper Lane", "Routing Broadway"],
            "snap_preventions": ["trunk", "ferry"],
            "curbsides": ["any", "right"],
            "details": ["tolls", "time"],
            "ch.disable": True,
            "custom_model": {
                "speed": [{"if": "true", "limit_to": "100"}],
                "priority": [{"if": "road_class == MOTORWAY", "multiply_by": "0"}],
                "distance_influence": 100,
            },
            "heading_penalty": 100,
            "pass_through": True,
            "turn_costs": True,
            "heading": [50, 50, 50],
            "fake_option": 42,
        },
    },
}

ENDPOINTS_ERROR_RESPONSES = {
    "google": {
        "ZERO_RESULTS": {
            "available_travel_modes": ["DRIVING", "WALKING", "BICYCLING"],
            "geocoded_waypoints": [{}, {}],
            "routes": [],
            "status": "ZERO_RESULTS",
        },
        "UNKNOWN_ERROR": {
            "available_travel_modes": ["DRIVING", "WALKING", "BICYCLING"],
            "geocoded_waypoints": [{}, {}],
            "routes": [],
            "status": "UNKNOWN_ERROR",
        },
    }
}
