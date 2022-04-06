DROP DATABASE IF EXISTS invinsense;
CREATE DATABASE invinsense;

use invinsense;

CREATE TABLE user_details(
         id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
         candidate_name varchar(255) NOT NULL,
         job_title varchar(255) NOT NULL,
         team_name varchar(255) NOT NULL
     );
     
INSERT INTO user_details(`candidate_name`, `job_title`, `team_name`) VALUES ('Kenil Ranpura','Backend Developer','Blue.OODA');
INSERT INTO user_details(`candidate_name`, `job_title`, `team_name`) VALUES ('Yash Bhatt','Backend Developer','Purple.ODS');
INSERT INTO user_details(`candidate_name`, `job_title`, `team_name`) VALUES ('Krupa Jani','Backend Developer','Blue.OODA');
INSERT INTO user_details(`candidate_name`, `job_title`, `team_name`) VALUES ('Bhavik Prajapati','Backend Developer','Blue.OODA');
INSERT INTO user_details(`candidate_name`, `job_title`, `team_name`) VALUES ('Jaydeep Kotak','Backend Developer','Red.RBAS');
INSERT INTO user_details(`candidate_name`, `job_title`, `team_name`) VALUES ('Vaibhavi Pandya','Backend Developer','Pink.GSOS');
INSERT INTO user_details(`candidate_name`, `job_title`, `team_name`) VALUES ('Vrutika pandya','Frontend Developer','Pink.GSOS');
INSERT INTO user_details(`candidate_name`, `job_title`, `team_name`) VALUES ('Hemang Gohil','Devops','Purple.ODS');
INSERT INTO user_details(`candidate_name`, `job_title`, `team_name`) VALUES ('Parth Thakkar','Backend Developer','Purple.ODS');


create table tools(id int(20) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    title varchar(255) NOT NULL,
    link varchar(255) NOT NULL,
    discription varchar(255),
    t_name varchar(255) NOT NULL,
    g_name varchar(255) NOT NULL
);


INSERT INTO tools(`title`,`discription`,`link`,`t_name`,`g_name`) VALUES ('SIER + EDR','Security Information and Event Management | Endpoint Detection and Response','https://wazuh.com','Wazuh','OODA');

INSERT INTO tools(`title`,`discription`,`link`,`t_name`,`g_name`) VALUES ('SOAR','Security Orchestration Automation & Response','https://shuffler.io','Shuffle','OODA');

INSERT INTO tools(`title`,`discription`,`link`,`t_name`,`g_name`) VALUES ('SOAR','Security Orchestration Automation & Response','https://thehive-project.org','TheHive','OODA');

INSERT INTO tools(`title`, `link`,`t_name`,`g_name`) VALUES ('Threat intel','https://www.infopercept.com','Infopercept','OODA');

INSERT INTO tools(`title`, `link`, `discription`,`t_name`,`g_name`) VALUES ('Threat Exchange','https://www.misp-project.org','Threat Exchange','MISP','OODA');

INSERT INTO tools(`title`, `link`, `discription`,`t_name`,`g_name`) VALUES ('Network Deception','https://linuxsecurity.expert/tools/dejavu/','On Premise','DejaVu','ODS');

INSERT INTO tools(`title`, `link`, `discription`,`t_name`,`g_name`) VALUES ('Network Deception','https://www.infopercept.com','On Cloud','Infopercept','ODS');

INSERT INTO tools(`title`, `link`,`t_name`,`g_name`) VALUES ('Patch Management','https://www.ansible.com','Ansible','ODS');

INSERT INTO tools(`title`, `link`,`t_name`,`g_name`) VALUES ('Endpoint Deception','https://deceptivebytes.com','Deceptive Bytes','ODS');

INSERT INTO tools(`title`, `link`,`t_name`,`g_name`) VALUES ('Vulnerability Management','https://www.defectdojo.org','DefectDOJO','RBAS');

INSERT INTO tools(`title`, `link`,`t_name`,`g_name`) VALUES ('Breach And Attack Simulation','https://caldera.mitre.org','Caldera','RBAS');

INSERT INTO tools(`title`, `link`,`t_name`,`g_name`) VALUES ('Breach And Attack Simulation','https://www.guardicore.com/infectionmonkey/','Infection Monkey','RBAS');

INSERT INTO tools(`title`, `link`,`t_name`,`g_name`) VALUES ('Red Ops','https://www.redelk.it/en','RedELK','RBAS');

INSERT INTO tools(`title`, `link`,`t_name`,`g_name`) VALUES ('Cloud Security Posture Management','https://www.crowdstrike.com/cybersecurity-101/cloud-security/cloud-security-posture-management-cspm/','Scout','RBAS');

INSERT INTO tools(`title`, `link`,`t_name`,`g_name`) VALUES ('Compliance Platform','https://www.infopercept.com','Infopercept','GSOS');

INSERT INTO tools(`title`, `link`,`t_name`,`g_name`) VALUES ('Enterprise Risk Management','https://www.simplerisk.com','SimpleRisk','GSOS');

INSERT INTO tools(`title`, `link`,`t_name`,`g_name`) VALUES ('Project Management','https://www.rukovoditel.net','Rukovoditel','GSOS');

CREATE TABLE `visits_log` (
  `id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `no_of_visits` int NULL,
  `ip_address` varchar(255) NULL,
  `requested_url` varchar(255) NULL,
  `referer_page` varchar(255) NULL,
  `page_name` varchar(255) NULL,
  `query_string` varchar(255) NULL,
  `user_agent` varchar(255) NULL,
  `access_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `method` varchar(255) NULL,
  `username` varchar(255) NULL,
  `tool_name` varchar(255) NULL
);
